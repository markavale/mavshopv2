from django.urls import reverse
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify # new
from taggit.managers import TaggableManager
import os
from PIL import Image

User = settings.AUTH_USER_MODEL

ITEM_TYPE = [
    ('Photoshop', 'Photoshop'),
    ('Lightroom', 'Lightroom'),
]

# Create your models here.
class Item(models.Model):
    title               = models.CharField(max_length=255, blank=False, null=False)
    slug                = models.SlugField(unique=True, max_length=255, null=False)
    description         = models.TextField(max_length=1000, blank=True, null=True)
    old_img             = models.ImageField(upload_to='shop', blank=True, null=True)
    new_img             = models.ImageField(upload_to='shop')
    price               = models.IntegerField(default=0, blank=True, null=True)
    discount_price      = models.IntegerField(blank=True, null=True)
    is_free             = models.BooleanField(blank=False, null=False)
    item_type           = models.CharField(max_length=255, choices=ITEM_TYPE)
    download_file       = models.FileField(upload_to='files')
    downloads           = models.PositiveIntegerField(default=0)
    views               = models.PositiveIntegerField(default=0)
    category            = models.ForeignKey('Categories',on_delete=models.CASCADE,related_name='item_categories')
    reviews             = models.ManyToManyField('Review', blank=True)
    tags                = TaggableManager()
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_computed_reviews(self):
        if self.reviews.count() != 0:
            sum = 0.0
            for review in self.reviews.all():
                sum += review.rate
            return round((sum / self.get_total_reviews()), 2)
        return 0

    def get_total_reviews(self):
        return int(self.reviews.count())

    def get_price(self):
        if self.is_free:
            return 0
        if self.discount_price:
            return self.discount_price
        return self.price

    def get_file_name(self):
        return self.download_file.name.split('/')[-1]

    def get_file_size(self):
        fullfilepath = ""
        fullfilepath = "media/" + os.path.getsize("{}".format(self.download_file))
        return fullfilepath

    def get_download_url(self):
        return reverse('download-file', kwargs={
            'slug':self.slug
        })

    def save(self, *args, **kwargs): # new
        super(Item,self).save(*args, **kwargs)

        if self.old_img:
            old_img = Image.open(self.old_img.path)
            if old_img and old_img.height > 2048 or old_img.width > 2048:
                output_size = (2048, 2048)
                old_img.thumbnail(output_size)
                old_img.save(self.old_img.path)

        if self.new_img:
            new_img = Image.open(self.new_img.path)
            if new_img and new_img.height > 2048 or new_img.width > 2048:
                output_size = (2048, 2048)
                new_img.thumbnail(output_size)
                new_img.save(self.new_img.path)

        if not self.slug:
            self.slug = slugify(self.title)
        
        # return super().save(*args, **kwargs)

class Review(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    rate            = models.FloatField(blank=False, null=False)
    message         = models.TextField(max_length=255, blank=True, null=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} rated {self.rate}'

class Categories(models.Model):
    category_name = models.CharField(max_length=255, blank=False, null=False)
    slug            = models.SlugField(unique=True, max_length=255)
    featured_image = models.ImageField(upload_to='featured_image',default='featured_image/default.jpg')
    category_type       = models.CharField(max_length=255, choices=ITEM_TYPE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def get_featured_image(self):
        image = self.featured_image
        if image and hasattr(image, 'url'):
            return image.url
        else:
            return '/media/featured_image/default.jpg'

    # def get_total_price(self):
    #     if self.discount_price:
    #         return self.discount_price
    #     return self.price

    # def get_amount_saved(self):
    #     if self.discount_price:
    #         return self.price - self.discount_price
    #     return None

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)

class OrderItem(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered          = models.BooleanField(default=False)
    item                = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_selected         = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.item}"

class Order(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code                = models.CharField(max_length=20, blank=True, null=True)
    items                   = models.ManyToManyField(OrderItem)
    start_date              = models.DateTimeField(auto_now_add=True)
    ordered_date            = models.DateTimeField(null=True, blank=True)
    ordered                 = models.BooleanField(default=False)  
    coupon                  = models.ForeignKey('Coupon',blank=True, null=True, 
    on_delete=models.SET_NULL)
    use_coupon              = models.BooleanField(default=False) 
    purchased               = models.BooleanField(default=False)
    refund_requested        = models.BooleanField(default=False)
    refund_granted          = models.BooleanField(default=False)
    # being_delivered         = models.BooleanField(default=False)
    # shipping_address        = models.ForeignKey('Address', related_name='shipping_address', on_delete=models.SET_NULL,
    #     blank=True, null=True)
    # billing_address         = models.ForeignKey('Address', related_name='billing_address', on_delete=models.SET_NULL,
    #     blank=True, null=True)
    # payment                 = models.ForeignKey('Payment', on_delete=models.SET_NULL,
    #     blank=True, null=True)  
    '''
    1. Added Item to cart
    2. adding a billing address # not applicable
    (Failed to checkout)
    3. Payment form
    (Preprocessing, processing, packaging, etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        if self.user:
            return self.user.username
        return "Annonymous User"

    def get_sub_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.item.get_price()
        return total

    def get_selected_items_sub_total(self):
        total = 0
        for order_item in self.items.filter(is_selected=True):
            total += order_item.item.get_price()
        return total

    def get_total(self):
        total = 0
        for order_item in self.items.filter(is_selected=True):
            total += order_item.item.get_price()
        if self.coupon and self.use_coupon:
            if self.coupon.amount > total:
                return total
            else:
                total -= self.coupon.amount
        return total
    
    def get_total_items(self):
        return self.items.count()

    def add_coupon(self, coupon):
        self.coupon = coupon
        self.use_coupon = True
        self.save()

    def remove_coupon(self):
        self.use_coupon = False
        self.coupon = None
        self.save()


class WishList(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    items               = models.ManyToManyField(Item)
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_total_items(self):
        return self.items.count()

class Coupon(models.Model):
    code            = models.CharField(max_length=255)
    amount          = models.FloatField()
    

    def __str__(self):
        return self.code

