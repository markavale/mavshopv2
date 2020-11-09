<template>
  <div>
    <div class="contact">
      <v-card :disabled="loading">
        <div class="container_box">
          <v-progress-linear
            :active="loading"
            :indeterminate="loading"
            height="5"
          ></v-progress-linear>
          <div class="row">
            <div class="col-md-6">
              <div class="title-box-2">
                <h5 class="title-left">Message Me</h5>
                <div style="float: right">
                  <TransitioningSmileyIcon :error="!valid" />
                </div>
              </div>
              <div>
                <v-form ref="form" v-model="valid" lazy-validation>
                  <v-text-field
                    v-model="name"
                    :counter="60"
                    :rules="nameRules"
                    label="Name"
                    required
                  ></v-text-field>

                  <v-text-field
                    v-model="subject"
                    :counter="60"
                    :rules="subjectRules"
                    label="Subject"
                  ></v-text-field>

                  <v-text-field
                    v-model="email"
                    :rules="emailRules"
                    label="E-mail"
                    required
                  ></v-text-field>

                  <v-textarea
                    name="input-7-1"
                    label="Message"
                    v-model="message"
                    :counter="255"
                    hint="It looks like we're going to have a wonderful work together!"
                    :rules="messageRules"
                    required
                    outline
                    class="mb-3"
                  ></v-textarea>

                  <v-btn
                    :disabled="!valid"
                    color="success"
                    class="mr-4"
                    @click.prevent="submitForm"
                  >
                    Submit
                  </v-btn>

                  <v-btn color="error" class="mr-4" @click="clearForm">
                    Clear Form
                  </v-btn>

                  <!-- <v-btn color="warning" @click="resetValidation">
                    Reset Validation
                  </v-btn> -->
                </v-form>
              </div>
            </div>
            <div class="col-md-6 xs-12">
              <div class="title-box-2 pt-4 pt-md-0">
                <h5 class="title-left">Live Preview</h5>
              </div>
              <v-card
                class="mx-auto overflow-y-auto"
                color="#f14336"
                dark
                min-height="auto"
                max-height="500px"
                max-width="100%"
              >
                <v-card-title>
                  <v-icon large left> mdi-gmail </v-icon>
                  <span class="title font-weight-light">Gmail</span>
                  <v-row align="center" justify="center">
                    <span
                      class="subheading font-weight-bold mr-2 px-2"
                      v-if="subject.length == 0"
                      >[ Email Subject ]</span
                    >
                    <span
                      class="subheading font-weight-bold mr-2 px-2"
                      v-else
                      >{{ subject }}</span
                    >
                  </v-row>
                </v-card-title>

                <v-card-text
                  class="headline font-weight-bold"
                  v-if="message.length == 0"
                >
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo
                  reiciendis veniam aut, ex enim culpa fugiat in sunt cupiditate
                  blanditiis? Architecto fuga tenetur suscipit at.
                </v-card-text>
                <v-card-text class="headline font-weight-bold" v-else>
                  {{ message }}
                </v-card-text>

                <v-card-actions>
                  <v-list-item class="grow">
                    <v-list-item-avatar color="grey darken-3">
                      <v-img
                        class="elevation-6"
                        alt=""
                        src='https://avataaars.io/?avatarStyle=Transparent&topType=LongHairDreads&accessoriesType=Prescription01&hairColor=Auburn&facialHairType=Blank&clotheType=Hoodie&clotheColor=PastelYellow&eyeType=Happy&eyebrowType=SadConcernedNatural&mouthType=Smile&skinColor=Light'
                      ></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title>
                        <span v-if="name.length == 0">John Doe</span>
                        <span v-else>{{ name }}</span>
                        <br />
                        <span v-if="email.length == 0" class="sender__email"
                          >johndoe@gmail.com</span
                        >
                        <span v-else class="sender__email">{{ email }}</span>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-card-actions>
              </v-card>
            </div>
          </div>
        </div>
      </v-card>
    </div>
  </div>
</template>

<script>
import TransitioningSmileyIcon from "@dexmo/vue-transitioning-result-icon";
export default {
  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 60) || "Name must be less than 60 characters",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    subject: "",
    subjectRules: [
      (v) => v.length <= 60 || "Subject must be less than 60 characters",
    ],
    message: "",
    messageRules: [
      (v) => !!v || "Message is required",
      (v) =>
        (v && v.length <= 255) || "Message must be less than 255 characters",
    ],
    errors: [],
    loading: false,
    sender: ""
  }),
  components: {
    TransitioningSmileyIcon,
  },
  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    submitForm() {
      this.loading = true
      this.$refs.form.validate();
      if (this.valid) {
        const payload = {
          name: this.name,
          subject: this.subject,
          email: this.email,
          message: this.message,
        };
        this.$store
          .dispatch("sendMail", payload)
          .then(() => {
            this.sender = this.name.split(" ")[0];
            this.clearForm();
            this.loading = false
            this.$toast.success({
            title: "Message has been sent",
            message: `Thank you, ${this.sender} for reaching out. I will response to you as soon as possible`,
            type: 'success',
            position: 'top right',
            icon: require('../../assets/icons/check-circle-white.png'),
            closeButton: true,
            timeOut: 5000,
            showDuration: 500,
            hideDuration: 500,
            showMethod: 'fadeIn',
            hideMethod: 'fadeOut',
            color: '#51A351',
          });
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
            let error_data = err.response.data;
            console.log(error_data);
            // console.log(error_data);
            for (const field_error in error_data) {
              this.errors.push(error_data[field_error][0]);
              console.log(error_data[field_error]);
            }
            
            console.log(this.errors);
            this.error = true;
          });
      }
    },
    clearForm(){
        this.name = ""
        this.subject = ""
        this.email = ""
        this.message = ""
        this.resetValidation();
    }
  },
};
</script>

<style>
.sender__email {
  font-style: italic;
  font-size: 13px;
}
.preview {
  background-color: #f5f5f5;
  height: 50vh;
  padding: 1.5rem 1.5rem;
}
.contact {
  margin: 70px;
}
.title-box-2 {
  margin-bottom: 3rem;
}

.title-left {
  font-size: 2rem;
  position: relative;
}

.title-left:before {
  content: "";
  position: absolute;
  height: 3px;
  background-color: #0078ff;
  width: 100px;
  bottom: -12px;
}

@media screen and (max-width: 992px) {
  .contact {
    margin: 35px;
  }
}

/* On screens that are 600px or less, set the background color to olive */
@media screen and (max-width: 600px) {
  .contact {
    margin: 20px;
  }
}
</style>