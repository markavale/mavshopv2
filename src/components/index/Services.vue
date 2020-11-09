<template>
  <div>
    <div class="container">
      <div class="row mt-5">
        <div class="col-sm-12">
          <div class="center">
            <h5 class="title-header center"
            style="font-size:3rem; font-weight:650">Services</h5>
            <div class="line-mf"></div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12 col-md-4">
          <div class="wrapper">
            <div class="card-flip">
              <input
                type="checkbox"
                id="card1"
                class="more"
                aria-hidden="true"
              />
              <div class="content">
                <div class="front" style="background-color: #15314b">
                  <div class="inner">
                    <h2>Web Development</h2>
                    <label for="card1" class="button" aria-hidden="true">
                      Details
                    </label>
                  </div>
                </div>
                <div class="back" style="background-color: #15314b">
                  <div class="inner">
                    <div class="info">
                      <span style="color: white; font-size: 25px; background-color:#15314b;"
                        >Web Development</span
                      >
                    </div>
                    <div class="description" style="color: white">
                      <p>
                        I'm using Python as programming language and Django as
                        back-end framework and HTML, CSS, and Javascript, VueJS,
                        and bootstrap on frontend.
                      </p>
                      <p>
                        I develop with passion and quality to meet the client's
                        expection.
                      </p>
                    </div>
                    <label for="card1" class="button return" aria-hidden="true">
                      <i class="fas fa-arrow-left" style="color: white"></i>
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm-12 col-md-4">
          <div class="wrapper">
            <div class="card-flip">
              <input
                type="checkbox"
                id="card2"
                class="more"
                aria-hidden="true"
              />
              <div class="content">
                <div class="front" style="background-color: #15314b">
                  <div class="inner">
                    <h2>Graphic Design</h2>

                    <label for="card2" class="button" aria-hidden="true">
                      Details
                    </label>
                  </div>
                </div>
                <div class="back" style="background-color: #15314b">
                  <div class="inner">
                    <div class="info">
                      <span style="color: white; font-size: 25px; background-color:#15314b;"
                        >Graphic Design</span
                      >
                    </div>
                    <div class="description" style="color: white">
                      <p>
                        I'm using Adobe Photoshop for my Graphic designs. I have
                        an experience designing a T-shirt, Web UI, Mobile UI,
                        Birthday Card, Vector Art, Photo Manipulation, Tarp
                        design and etc.
                      </p>
                      <p>
                        I just love how I turn my ideas into a graphic design.
                      </p>
                    </div>
                    <label for="card2" class="button return" aria-hidden="true">
                      <i class="fas fa-arrow-left" style="color: white"></i>
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm-12 col-md-4">
          <div class="wrapper">
            <div class="card-flip">
              <input
                type="checkbox"
                id="card3"
                class="more"
                aria-hidden="true"
              />
              <div class="content">
                <div class="front" style="background-color: #15314b">
                  <div class="inner">
                    <h2>Lightroom Presets</h2>

                    <label for="card3" class="button" aria-hidden="true">
                      Details
                    </label>
                  </div>
                </div>
                <div class="back" style="background-color: #15314b">
                  <div class="inner">
                    <div class="info">
                      <span style="color: white; font-size: 25px; background-color:#15314b;"
                        >Lightroom Presets</span
                      >
                    </div>
                    <div class="description" style="color: white">
                      <p>
                        I'm using Adobe Classic Lightroom CC for making
                        lightroom presets. It will be available to purchase soon
                        when the development of my ecommerce website is done.
                      </p>
                      <p>
                        You can check out my Instagram @markavale_ to see a few
                        of my presets.
                      </p>
                    </div>
                    <label for="card3" class="button return" aria-hidden="true">
                      <i class="fas fa-arrow-left" style="color: white"></i>
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.wrapper {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
}

.card-flip {
  width: 420px;
  height: 340px;
  margin: 1em;
  perspective: 1500px;
}
.card-flip .content {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.8s cubic-bezier(0.75, 0, 0.85, 1);
}

.more {
  display: none;
}
.more:checked ~ .content {
  transform: rotateY(180deg);
}

.front,
.back {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  transform-style: preserve-3d;
  border-radius: 6px;
}
.front .inner,
.back .inner {
  height: 100%;
  display: grid;
  padding: 1.5em;
  transform: translateZ(80px) scale(0.94);
}
.inner >.info span{
  font-size:25px;
}
.front {
  background-color: #fff;
  background-size: cover;
  background-position: center center;
}
.front:after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 6px;
  backface-visibility: hidden;
  /* background: linear-gradient(40deg, rgba(67, 138, 243, 0.7), rgba(255, 242, 166, 0.7)); */
  background: linear-gradient(40deg, rgba(21, 49, 75, 0.7), rgba(0, 120, 255,0.7));
}
.front .inner {
  grid-template-rows: 5fr 1fr 1fr 2fr 1fr;
  justify-items: center;
}
.front h2 {
  grid-row: 2;
  margin-bottom: 0.3em;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: #fff;
  font-weight: 500;
  text-shadow: 0 0 6px rgba(0, 0, 0, 0.1);
}
.front .rating {
  grid-row: 3;
  color: rgba(255, 255, 255, 0.8);
  font-size: 14px;
  display: flex;
  flex-flow: row nowrap;
}
.front .rating i {
  margin: 0 1px;
}

.back {
  transform: rotateY(180deg);
  background-color: #fff;
  border: 2px solid #f0f0f0;
}
.back .inner {
  grid-template-rows: 1fr 2fr 1fr 2fr 14fr 1fr 1fr;
  grid-template-columns: repeat(4, auto);
  grid-column-gap: 0.8em;
  justify-items: center;
}
.back .info {
  position: relative;
  display: flex;
  align-items: center;
  color: #355cc9;
  grid-row: 3;
}
.back .info:not(:first-of-type):before {
  content: '';
  position: absolute;
  left: -0.9em;
  height: 18px;
  width: 1px;
  background-color: #ccc;
}
.back .info span {
  font-size: 2em;
  font-weight: 700;
}
.back .info i {
  font-size: 1.2em;
}
.back .info i:before {
  background: linear-gradient(40deg, #355cc9, #438af3);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}
.back .info .icon {
  margin-left: 0.3em;
}
.back .info .icon span {
  display: block;
  margin-top: -0.25em;
  font-size: 0.8em;
  font-weight: 600;
  white-space: nowrap;
}
.back .description {
  grid-row: 5;
  grid-column: 1/-1;
  font-size: 1em;
  border-radius: 5px;
  font-weight: 600;
  line-height: 1.4em;
  overflow: auto;
  color: #355cc9;
  padding-right: 10px;
  
}
.back .location,
.back .price {
  font-weight: 600;
  color: #355cc9;
  grid-row: 1;
  font-size: 0.86em;
}
.back .location {
  grid-column: 1/3;
  justify-self: left;
}
.back .price {
  grid-column: 3/-1;
  justify-self: right;
}
.back .button {
  grid-column: 1/-1;
  justify-self: center;
}

.button {
  grid-row: -1;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
  cursor: pointer;
  display: block;
  padding: 0 1.5em;
  height: 3em;
  line-height: 2.9em;
  min-width: 3em;
  background-color: transparent;
  border: solid 2px #fff;
  color: #fff;
  border-radius: 4px;
  text-align: center;
  left: 50%;
  backface-visibility: hidden;
  transition: 0.3s ease-in-out;
  text-shadow: 0 0 6px rgba(0, 0, 0, 0.3);
}
.button:hover {
  background-color: #fff;
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.5);
  text-shadow: none;
  color: #355cc9;
}
.button.return {
  line-height: 3em;
  color: #355cc9;
  border-color: #355cc9;
  text-shadow: none;
}
.button.return:hover {
  background-color: #355cc9;
  color: #fff;
  box-shadow: none;
}

::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #859ddf;
}

::-webkit-scrollbar-thumb:hover {
  background: #355cc9;
}


/* simple card flip */
.portfolio-icons > a{
  color:#15314b;
  font-size:20px;
  font-weight: 500;
}
.card-simple-flip {
  width: 300px;
  height: 250px;
  background: #000;
  border-radius: 1rem;
  margin:10px auto;
}
.card-simple-flip .image-card {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-color:#0078ff;
}
.card-simple-flip .image-card img {
  width: 150px;
  transition: .5s;
  height:150px;
  margin:50px 0;
}
.card-simple-flip:hover .image-card img {
  opacity: .5;
  transform: translateX(30%);/*100%*/
}
.card-simple-flip .details {
  position: absolute;
  top: 0;
  left: 0;
  width: 70%;/*100%*/
  height: 100%;
  background: #ffc107;
  transition: .5s;
  transform-origin: left;
  transform: perspective(2000px) rotateY(-90deg);
}
.card-simple-flip:hover .details {
  transform: perspective(2000px) rotateY(0deg);
}
.card-simple-flip .details .center {
  padding: 20px;
  text-align: center;
  background: #fff;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
.card-simple-flip .details .center h1 {
  margin: 0;
  padding: 0;
  color: #15314b;
  line-height: 20px;
  font-size: 20px;
  text-transform: uppercase;
}
.card-simple-flip .details .center h1 span {
  font-size: 14px;
  color: #262626;
}
.card-simple-flip .details .center p {
  margin: 10px 0;
  padding: 0;
  color: #262626;
}
.card-simple-flip .details .center ul {
  margin: 10px auto 0;
  padding: 0;
  display: table;
}
.card-simple-flip .details .center ul li {
  list-style: none;
  margin: 0 5px;
  float: left;
}
.card-simple-flip .details .center ul li a {
  display: block;
  background: #262626;
  color: #fff;
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  transform: .5s;
}
.card-simple-flip .details .center ul li a:hover {
  background: #ff3636;
}
/* end */

@media screen and (min-width: 300px) and (max-width:767px){
  .card__collection{
    padding:10px;
    margin-right:5px;
  }
  .img-responsive{
    margin:0 auto;
  }
}
</style>