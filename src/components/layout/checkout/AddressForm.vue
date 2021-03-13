<template>
  <div>
    <div class="d-flex">
      <v-icon color="red">mdi-map-marker</v-icon>
      <p class="title my-auto">Billing Address</p>
    </div>
    <v-divider></v-divider>
    <form>
      <v-row dense>
        <v-col cols="6">
          <v-text-field
            v-model="first_name"
            :error-messages="firstNameErrors"
            label="First name"
            required
            @input="$v.first_name.$touch()"
            @blur="$v.first_name.$touch()"
            dense
            filled
            prepend-inner-icon="mdi-account"
          ></v-text-field>
        </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="last_name"
            :error-messages="lastNameErrors"
            label="Last name"
            prepend-inner-icon="mdi-account"
            required
            @input="$v.last_name.$touch()"
            @blur="$v.last_name.$touch()"
            dense
            filled
          ></v-text-field>
        </v-col>
      </v-row>
      <v-country-select
        v-model="country"
        :country-name="countryName"
        required
        dense
        filled
        placeholder=""
        prepend-inner-icon="mdi-map-marker"
        label="Country/region"
        :error-messages="countryErrors"
      />
      <v-region-select
        v-model="region"
        :country="country"
        :country-name="countryName"
        prepend-inner-icon="mdi-map-marker"
        required
        dense
        filled
        label="State/province/region"
        :error-messages="regionErrors"
      />
      <v-text-field
        v-model="city"
        :error-messages="cityErrors"
        label="City"
        prepend-inner-icon="mdi-map-marker"
        required
        @input="$v.city.$touch()"
        @blur="$v.city.$touch()"
        dense
        filled
      ></v-text-field>

      <v-text-field
        v-model="address1"
        :error-messages="address1Errors"
        label="Address"
        hint="Street,building,area,C/O,etc."
        persistent-hint
        prepend-inner-icon="mdi-map-marker"
        required
        @input="$v.address1.$touch()"
        @blur="$v.address1.$touch()"
        dense
        filled
      ></v-text-field>
      <v-text-field
        v-model="address2"
        :error-messages="address2Errors"
        label="Address 2(optional)"
        hint="Floor no.,House No.,etc"
        persistent-hint
        prepend-inner-icon="mdi-map-marker"
        required
        @input="$v.address2.$touch()"
        @blur="$v.address2.$touch()"
        dense
        filled
      ></v-text-field>
      <v-text-field
        v-model="zip"
        :error-messages="zipErrors"
        label="Zip/postal code"
        prepend-inner-icon="mdi-map-marker"
        required
        @input="$v.zip.$touch()"
        @blur="$v.zip.$touch()"
        dense
        filled
      ></v-text-field>
      <!-- <v-text-field
        v-model="email"
        :error-messages="emailErrors"
        label="E-mail"
        required
        @input="$v.email.$touch()"
        @blur="$v.email.$touch()"
        dense
        filled
      ></v-text-field> -->
      <!-- <v-checkbox
        v-model="checkbox"
        :error-messages="checkboxErrors"
        label="Do you agree?"
        required
        @change="$v.checkbox.$touch()"
        @blur="$v.checkbox.$touch()"
      ></v-checkbox> -->

      <v-btn class="mr-4" color="green" dark @click="submit"> Save </v-btn>
      <v-btn @click="clear"> clear </v-btn>
    </form>

    <div class="payment__section">
      <div class="d-flex">
      <v-icon color="blue"> mdi-credit-card-multiple</v-icon>
      <p class="title my-auto ml-1">Paymet method</p>
    </div>
    <v-divider></v-divider>
    </div>
    
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { countries } from "./countries";
import { required, maxLength } from "vuelidate/lib/validators";
// import vueCountryRegionSelect from 'vue-country-region-select'
export default {
  mixins: [validationMixin],

  validations: {
    name: { required, maxLength: maxLength(10) },
    first_name: { required, maxLength: maxLength(50) },
    last_name: { required, maxLength: maxLength(50) },
    // email: { required, email },
    country: { required },
    region: { required },
    city: { required, maxLength: maxLength(255) },
    address1: { required, maxLength: maxLength(255) },
    address2: { required, maxLength: maxLength(255) },
    zip: { required, maxLength: maxLength(10) },
    checkbox: {
      checked(val) {
        return val;
      },
    },
  },

  data: () => ({
    first_name: "",
    last_name: "",
    name: "",
    // email: "",
    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,
    country: "",
    countryName: true,
    region: "",
    city: "",
    address1: "",
    address2: "",
    zip: null,
  }),
  components: {
    // vueCountryRegionSelect,
  },
  computed: {
    checkboxErrors() {
      const errors = [];
      if (!this.$v.checkbox.$dirty) return errors;
      !this.$v.checkbox.checked && errors.push("You must agree to continue!");
      return errors;
    },
    firstNameErrors() {
      const errors = [];
      if (!this.$v.first_name.$dirty) return errors;
      !this.$v.first_name.maxLength &&
        errors.push("First name must be at most 50 characters long");
      !this.$v.first_name.required && errors.push("First name is required.");
      return errors;
    },
    lastNameErrors() {
      const errors = [];
      if (!this.$v.last_name.$dirty) return errors;
      !this.$v.last_name.maxLength &&
        errors.push("Last name must be at most 50 characters long");
      !this.$v.last_name.required && errors.push("Last name is required.");
      return errors;
    },
    // emailErrors() {
    //   const errors = [];
    //   if (!this.$v.email.$dirty) return errors;
    //   !this.$v.email.email && errors.push("Must be valid e-mail");
    //   !this.$v.email.required && errors.push("E-mail is required");
    //   return errors;
    // },
    countryErrors() {
      const errors = [];
      if (!this.$v.country.$dirty) return errors;
      !this.$v.country.required && errors.push("Country is required");
      return errors;
    },
    regionErrors() {
      const errors = [];
      if (!this.$v.region.$dirty) return errors;
      !this.$v.region.required && errors.push("Region is required");
      return errors;
    },
    cityErrors() {
      const errors = [];
      if (!this.$v.city.$dirty) return errors;
      !this.$v.city.maxLength &&
        errors.push("City name must be at most 50 characters long");
      !this.$v.city.required && errors.push("City name is required.");
      return errors;
    },
    address1Errors() {
      const errors = [];
      if (!this.$v.address1.$dirty) return errors;
      !this.$v.address1.maxLength &&
        errors.push("Address must be at most 255 characters long");
      !this.$v.address1.required && errors.push("Address is required.");
      return errors;
    },
    address2Errors() {
      const errors = [];
      if (!this.$v.address2.$dirty) return errors;
      !this.$v.address2.maxLength &&
        errors.push("Address must be at most 255 characters long");
      !this.$v.address2.required && errors.push("Address is required.");
      return errors;
    },
    zipErrors() {
      const errors = [];
      if (!this.$v.zip.$dirty) return errors;
      !this.$v.zip.maxLength &&
        errors.push("Zip code must be at most 10 characters long");
      !this.$v.zip.required && errors.push("Zip code is required.");
      return errors;
    },
  },
  mounted() {
    console.log(countries);
  },
  methods: {
    submit() {
      this.$v.$touch();
    },
    clear() {
      this.$v.$reset();
      this.name = "";
      this.first_name = "";
      this.last_name = "";
      // this.email = "";
      this.select = null;
      this.checkbox = false;
      this.country = "";
      this.region = "";
      this.city = "";
      this.address1 = "";
      this.address2 = "";
      this.zip = null;
    },
  },
};
</script>

<style>
.payment__section{
  margin: 70px 0;
}
</style>