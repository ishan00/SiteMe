#type=orange
@import url(http://fonts.googleapis.com/css?family=Raleway);
#cssmenu,
#cssmenu ul,
#cssmenu ul li,
#cssmenu ul li a {
  margin: 0;
  padding: 0;
  border: 0;
  list-style: none;
  line-height: 1;
  display: block;
  position: relative;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
#cssmenu:after,
#cssmenu > ul:after {
  content: ".";
  display: block;
  clear: both;
  visibility: hidden;
  line-height: 0;
  height: 0;
}
#cssmenu {
  width: auto;
  border-bottom: 3px solid #47c9af;
  font-family: Raleway, sans-serif;
  line-height: 1;
}
#cssmenu ul {
  background: #ffffff;
}
#cssmenu > ul > li {
  float: left;
}
#cssmenu.align-center > ul {
  font-size: 0;
  text-align: center;
}
#cssmenu.align-center > ul > li {
  display: inline-block;
  float: none;
}
#cssmenu.align-right > ul > li {
  float: right;
}
#cssmenu.align-right > ul > li > a {
  margin-right: 0;
  margin-left: -4px;
}
#cssmenu > ul > li > a {
  z-index: 2;
  padding: 18px 25px 12px 25px;
  font-size: 15px;
  font-weight: 400;
  text-decoration: none;
  color: #444444;
  -webkit-transition: all .2s ease;
  -moz-transition: all .2s ease;
  -ms-transition: all .2s ease;
  -o-transition: all .2s ease;
  transition: all .2s ease;
  margin-right: -4px;
}
#cssmenu > ul > li.active > a,
#cssmenu > ul > li:hover > a,
#cssmenu > ul > li > a:hover {
  color: #ffffff;
}
#cssmenu > ul > li > a:after {
  position: absolute;
  left: 0;
  bottom: 0;
  right: 0;
  z-index: -1;
  width: 100%;
  height: 120%;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  content: "";
  -webkit-transition: all .2s ease;
  -o-transition: all .2s ease;
  transition: all .2s ease;
  -webkit-transform: perspective(5px) rotateX(2deg);
  -webkit-transform-origin: bottom;
  -moz-transform: perspective(5px) rotateX(2deg);
  -moz-transform-origin: bottom;
  transform: perspective(5px) rotateX(2deg);
  transform-origin: bottom;
}
#cssmenu > ul > li.active > a:after,
#cssmenu > ul > li:hover > a:after,
#cssmenu > ul > li > a:hover:after {
  background: #47c9af;
}
------------------------------------------------------------------------------------------------------
@import url(http://fonts.googleapis.com/css?family=Open+Sans:700);
#cssmenu {
  background: #f96e5b;
  width: auto;
}
#cssmenu ul {
  list-style: none;
  margin: 0;
  padding: 0;
  line-height: 1;
  display: block;
  zoom: 1;
}
#cssmenu ul:after {
  content: " ";
  display: block;
  font-size: 0;
  height: 0;
  clear: both;
  visibility: hidden;
}
#cssmenu ul li {
  display: inline-block;
  padding: 0;
  margin: 0;
}
#cssmenu.align-right ul li {
  float: right;
}
#cssmenu.align-center ul {
  text-align: center;
}
#cssmenu ul li a {
  color: #ffffff;
  text-decoration: none;
  display: block;
  padding: 15px 25px;
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 14px;
  position: relative;
  -webkit-transition: color .25s;
  -moz-transition: color .25s;
  -ms-transition: color .25s;
  -o-transition: color .25s;
  transition: color .25s;
}
#cssmenu ul li a:hover {
  color: #333333;
}
#cssmenu ul li a:hover:before {
  width: 100%;
}
#cssmenu ul li a:after {
  content: "";
  display: block;
  position: absolute;
  right: -3px;
  top: 19px;
  height: 6px;
  width: 6px;
  background: #ffffff;
  opacity: .5;
}
#cssmenu ul li a:before {
  content: "";
  display: block;
  position: absolute;
  left: 0;
  bottom: 0;
  height: 3px;
  width: 0;
  background: #333333;
  -webkit-transition: width .25s;
  -moz-transition: width .25s;
  -ms-transition: width .25s;
  -o-transition: width .25s;
  transition: width .25s;
}
#cssmenu ul li.active a {
  color: #333333;
}
#cssmenu ul li.active a:before {
  width: 100%;
}
#cssmenu.align-right li:first-child a:after {
  display: none;
}
@media screen and (max-width: 768px) {
  #cssmenu ul li {
    float: none;
    display: block;
  }
  #cssmenu ul li a {
    width: 100%;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    border-bottom: 1px solid #fb998c;
  }
  #cssmenu ul li a:after {
    display: none;
  }
  #cssmenu ul li a:before {
    display: none;
  }
}
-------------------------------------------------------------------------------------------
@import url(http://fonts.googleapis.com/css?family=Lato:300,400,700);
@charset "UTF-8";
/* Base Styles */
#cssmenu ul,
#cssmenu li,
#cssmenu a {
  list-style: none;
  margin: 0;
  padding: 0;
  border: 0;
  line-height: 1;
  font-family: 'Lato', sans-serif;
}
#cssmenu {
  border: 1px solid #133e40;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
  width: auto;
}
#cssmenu ul {
  zoom: 1;
  background: #36b0b6;
  background: -moz-linear-gradient(top, #36b0b6 0%, #2a8a8f 100%);
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #36b0b6), color-stop(100%, #2a8a8f));
  background: -webkit-linear-gradient(top, #36b0b6 0%, #2a8a8f 100%);
  background: -o-linear-gradient(top, #36b0b6 0%, #2a8a8f 100%);
  background: -ms-linear-gradient(top, #36b0b6 0%, #2a8a8f 100%);
  background: linear-gradient(top, #36b0b6 0%, #2a8a8f 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='@top-color', endColorstr='@bottom-color', GradientType=0);
  padding: 5px 10px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
}
#cssmenu ul:before {
  content: '';
  display: block;
}
#cssmenu ul:after {
  content: '';
  display: table;
  clear: both;
}
#cssmenu li {
  float: left;
  margin: 0 5px 0 0;
  border: 1px solid transparent;
}
#cssmenu li a {
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
  padding: 8px 15px 9px 15px;
  display: block;
  text-decoration: none;
  color: #ffffff;
  border: 1px solid transparent;
  font-size: 16px;
}
#cssmenu li.active {
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
  border: 1px solid #36b0b6;
}
#cssmenu li.active a {
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
  display: block;
  background: #1e6468;
  border: 1px solid #133e40;
  -moz-box-shadow: inset 0 5px 10px #133e40;
  -webkit-box-shadow: inset 0 5px 10px #133e40;
  box-shadow: inset 0 5px 10px #133e40;
}
#cssmenu li:hover {
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
  border: 1px solid #36b0b6;
}
#cssmenu li:hover a {
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
  display: block;
  background: #1e6468;
  border: 1px solid #133e40;
  -moz-box-shadow: inset 0 5px 10px #133e40;
  -webkit-box-shadow: inset 0 5px 10px #133e40;
  box-shadow: inset 0 5px 10px #133e40;
}
-------------------------------------------------------------------------------------------------
.wrap {
  display: inline-block;
  -webkit-box-shadow: 0 0 70px #fff;
  -moz-box-shadow: 0 0 70px #fff;
  box-shadow: 0 0 70px #fff;
  margin-top: 40px;
}

/* a little "umph" */
.decor {
  background: #6EAF8D;
  background: -webkit-linear-gradient(left, #CDEBDB 50%, #6EAF8D 50%);
  background: -moz-linear-gradient(left, #CDEBDB 50%, #6EAF8D 50%);
  background: -o-linear-gradient(left, #CDEBDB 50%, #6EAF8D 50%);
  background: linear-gradient(left, white 50%, #6EAF8D 50%);
  background-size: 50px 25%;;
  padding: 2px;
  display: block;
}

a {
  text-decoration: none;
  color: #fff;
  display: block;
}

ul {
  list-style: none;
  position: relative;
  text-align: left;
}

li {
  float: left;
}

/* clear'n floats */
ul:after {
  clear: both;
}

ul:before,
ul:after {
    content: " ";
    display: table;
}

nav {
  position: relative;
  background: #2B2B2B;
  background-image: -webkit-linear-gradient(bottom, #2B2B2B 7%, #333333 100%);
  background-image: -moz-linear-gradient(bottom, #2B2B2B 7%, #333333 100%);
  background-image: -o-linear-gradient(bottom, #2B2B2B 7%, #333333 100%);
  background-image: linear-gradient(bottom, #2B2B2B 7%, #333333 100%);
  text-align: center;
  letter-spacing: 1px;
  text-shadow: 1px 1px 1px #0E0E0E;
  -webkit-box-shadow: 2px 2px 3px #888;
  -moz-box-shadow: 2px 2px 3px #888;
  box-shadow: 2px 2px 3px #888;
  border-bottom-right-radius: 8px;
  border-bottom-left-radius: 8px;
}

/* prime */
ul.primary li a {
  display: block;
  padding: 20px 30px;
  border-right: 1px solid #3D3D3D;
}

ul.primary li:last-child a {
  border-right: none;
}

ul.primary li a:hover {
  
  color: #000;
}

/* subs */
ul.sub {
  position: absolute;
  z-index: 200;
  box-shadow: 2px 2px 0 #BEBEBE;
  width: 35%;
  display:none;
}

ul.sub li {
  float: none;
  margin: 0;
}

ul.sub li a {
  border-bottom: 1px dotted #ccc;
  border-right: none;
  color: #000;
  padding: 15px 30px;
}

ul.sub li:last-child a {
  border-bottom: none;
}

ul.sub li a:hover {
  color: #000;
  background: #eeeeee;
}

/* sub display*/
ul.primary li:hover ul {
  display: block;
  background: #fff;
}

/* keeps the tab background white */
ul.primary li:hover a {
  background: #fff;
  color: #666;
  text-shadow: none;
}

ul.primary li:hover > a{
  color: #000;
} 

@media only screen and (max-width: 600px) {
  .decor {
    padding: 3px;
  }
  
  .wrap {
    width: 100%;
    margin-top: 0px;
  }
  
   li {
    float: none;
  }
  
  ul.primary li:hover a {
    background: none;
    color: #8B8B8B;
    text-shadow: 1px 1px #000;
  }

  ul.primary li:hover ul {
    display: block;
    background: #272727;
    color: #fff;
  }
  
  ul.sub {
    display: block;  
    position: static;
    box-shadow: none;
    width: 100%;
  }
  
  ul.sub li a {
    background: #272727;
    border: none;
    color: #8B8B8B;
  }
  
  ul.sub li a:hover {
    color: #ccc;
    background: none;
  }
}
-----------------------------------------------------------------------------------------------------
@import url(https://fonts.googleapis.com/css?family=Allan);
@import url(https://fonts.googleapis.com/css?family=Droid+Sans);
header{
      position: relative;
      background-color: #2c353a;
}
header ul.nav{
    overflow: hidden;
}
header ul.nav li{
    position: relative;
      float: left;
      width: 20%;
}
header ul.nav li a{
    display: block;
      height: 50px;
  opacity: 0;
  font: 400 1.15em 'Allan', serif;
      line-height: 50px;
      color: #848e92;
  text-decoration: none;
      text-align: center;
    cursor: default;
      -webkit-transition: all 0.25s ease;
    -moz-transition: all 0.25s ease;
  &:hover{
    color: #fff;
        background-color: #222b2f;
  }
}

@media screen and (max-width: 600px){
    header ul.nav li{
            float: none;
            width: 100%;
    }
      header ul.nav li a{
            height: 0;
    }
}

/* Style for header with active class name */

header.active ul.nav li a{
      height: 120px;
    opacity: 1;
      line-height: 120px;
      cursor: pointer;
}

@media screen and (max-width: 600px){
    header.active ul.nav li a{
            height: 60px;
            line-height: 60px;
    border-bottom: 1px solid #222b2f;
      }
}

/* Style for the plus button */

button.toggle-nav{
    position: absolute;
  top: 50px;
    left: calc(50% - 30px);
    width: 60px;
      height: 35px;
    background-color: #38a6a6;
  font: 400 1.2em 'Allan', serif;
    color: #fff;
  border: none;
    line-height: 30px;
    vertical-align: middle;
      outline: none;
  cursor: pointer;
    border-bottom-left-radius: 10px;
      border-bottom-right-radius: 10px;
      -webkit-transition: all 0.25s ease;
      -moz-transition: all 0.25s ease;
}
button.toggle-nav:hover{
    height: 50px;
}
button.toggle-nav span{
      display: block;
    -webkit-transform: rotate(90deg);
    -moz-transform: rotate(90deg);
    -webkit-transition: all 0.25s ease;
    -moz-transition: all 0.25s ease;
}

/* Style for the plus button when header has active classe name */

header.active button.toggle-nav{
    top: 120px;
  background-color: #256f6f;
}
header.active button.toggle-nav span{
      -webkit-transform: rotate(270deg);
    -moz-transform: rotate(270deg);
}

@media screen and (max-width: 600px){
      button.toggle-nav{
            top: 0;
            left: 15px;
      }
    header.active button.toggle-nav{
            top: 305px;
      }
}

/* Other styles */

.loud{
      text-transform: uppercase;
}
section{
  padding: 3em;
}
h1{
  margin: 1em 0;
  font-size: 40px;
  line-height: 1.5em;
}
p{
  margin: 1em 0;
}
strong{
  color: #93969c;
}

@media screen and (max-width: 600px){
  section{
    padding: 1.5em;
  }
}

-------------------------------------------------------------------------------------------------------------------
*, *:after,*:before{
    box-sizing: inherit;
}
a{
    color: #333;
    text-decoration: none;
}
h1{
  width: 100%;
  text-align: center;
  padding: 40px 0;
}
.open{
    position: fixed;
    top: 40px;
    right: 40px;
    width: 50px;
    height: 50px;
    display: block;
    cursor: pointer;
    transition: opacity 0.2s linear;
    &:hover{
        opacity: 0.8;
    }
    span{
        display: block;
        float: left;
        clear: both;
        height: 4px;
        width: 40px;
        border-radius: 40px;
        background-color: #fff;
        position: absolute;
        right: 3px;
        top: 3px;
        overflow: hidden;
        transition: all 0.4s ease;
        &:nth-child(1){
            margin-top: 10px;
            z-index: 9;
        }
        &:nth-child(2){
            margin-top: 25px;
        }
        &:nth-child(3){
            margin-top: 40px;
        }
    }
}
.sub-menu{
    transition: all 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        height: 0;
        width: 0;
        right: 0;
        top: 0;
        position: absolute;
        background-color: rgba(38, 84, 133, 0.54);
        border-radius: 50%;
        z-index: 18;
        overflow: hidden;
        li{
            display: block;
            float: right;
            clear: both;
            height: auto;
            margin-right: -160px;
            transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            &:first-child{
                margin-top: 180px;
            }
            &:nth-child(1){
                -webkit-transition-delay: 0.05s;
            }
            &:nth-child(2){
                -webkit-transition-delay: 0.10s;
            }
            &:nth-child(3){
                -webkit-transition-delay: 0.15s;
            }
            &:nth-child(4){
                -webkit-transition-delay: 0.20s;
            }
            &:nth-child(5){
                -webkit-transition-delay: 0.25s;
            }
            a{
                color: #fff;
                font-family: 'Lato', Arial, Helvetica, sans-serif;
                font-size: 16px;
                width: 100%;
                display: block;
                float: left;
                line-height: 40px;
            }
        }
    }

    .oppenned{
        .sub-menu{
            opacity: 1;
            height: 400px;
            width: 400px;
        }
        span:nth-child(2){
            overflow: visible;
        }
        span:nth-child(1), span:nth-child(3){
            z-index: 100;
            transform: rotate(45deg);
        }
        span:nth-child(1){
            transform: rotate(45deg) translateY(12px) translateX(12px);
        }
        span:nth-child(2){
            height: 400px;
            width: 400px;
            right: -160px;
            top: -160px;
            border-radius: 50%;
            background-color: rgba(38, 84, 133, 0.54);
        }
        span:nth-child(3){          
            transform: rotate(-45deg) translateY(-10px) translateX(10px);
        }
        li{
            margin-right: 168px;
        }
    }
.button{
    display: block;
    float: left;
  clear: both;
    padding: 20px 40px;
    background: #fff;
    border-radius: 3px;
    border: 2px solid #10a1ea;
    overflow: hidden;
    position: relative;
    &:after{
        transition: transform 0.3s ease;
        content: "";
        position: absolute;
        height: 200px;
        width: 400px;
        transform: rotate(45deg) translateX(-540px) translateY(-100px);
        background: #10a1ea;
        z-index: 1;
    }
    &:before{
        transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        content: attr(title);
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        color: #fff;
        z-index: 2;
        text-align: center;
        padding: 20px 40px;
        transform: translateY(200px);
    }
    &:hover{
        text-decoration: none;
        &:after{
            transform: translateX(-300px) translateY(-100px);
        }
        &:before{
            transform: translateY(0);
        }
    }
}
------------------------------------------------------------------------------------------------------------------------------
@import url('https://fonts.googleapis.com/css?family=Open+Sans');
*, *:before, *:after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.cf {
  &:before, &:after { content: ' '; display: table; }
  &:after { clear: both; }
}

.title {
  padding: 50px 0;
  font-size: 24px;
  text-align: center;
}

.inner {
  max-width: 820px;
  margin: 0 auto;
}

.breadcrumbs {
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  background-color: #f5f5f5;
}

.breadcrumbs ul {
  border-left: 1px solid #ddd;
  border-right: 1px solid #ddd;
}

.breadcrumbs li {
  float: left;
  width: 20%;
}

.breadcrumbs a {
  position: relative;
  display: block;
  padding: 20px;
  padding-right: 0 !important; /* important overrides media queries */
  font-size: 13px;
  font-weight: bold;
  text-align: center;
  color: #aaa;
  cursor: pointer;
}

.breadcrumbs a:hover {
  background: #eee;
}

.breadcrumbs a.active {
  color: #777;
  background-color: #fafafa;
}

.breadcrumbs a span:first-child {
  display: inline-block;
  width: 22px;
  height: 22px;
  padding: 2px;
  margin-right: 5px;
  border: 2px solid #aaa;
  border-radius: 50%;
  background-color: #fff;
}

.breadcrumbs a.active span:first-child {
  color: #fff;
  border-color: #777;
  background-color: #777;
}

.breadcrumbs a:before,
.breadcrumbs a:after {
  content: '';
  position: absolute;
  top: 0;
  left: 100%;
  z-index: 1;
  display: block;
  width: 0;
  height: 0;
  border-top: 32px solid transparent;
  border-bottom: 32px solid transparent;
  border-left: 16px solid transparent;
}

.breadcrumbs a:before {
  margin-left: 1px;
  border-left-color: #d5d5d5;
}

.breadcrumbs a:after {
  border-left-color: #f5f5f5;
}

.breadcrumbs a:hover:after {
  border-left-color: #eee;
}

.breadcrumbs a.active:after {
  border-left-color: #fafafa;
}

.breadcrumbs li:last-child a:before,
.breadcrumbs li:last-child a:after {
  display: none;
}

@media (max-width: 720px) { 
  .breadcrumbs a {
    padding: 15px;
  }
  .breadcrumbs a:before,
  .breadcrumbs a:after {
    border-top-width: 26px;
    border-bottom-width: 26px;
    border-left-width: 13px;
  }
}

@media (max-width: 620px) { 
  .breadcrumbs a {
    padding: 10px;
    font-size: 12px;
  }
  .breadcrumbs a:before,
  .breadcrumbs a:after {
    border-top-width: 22px;
    border-bottom-width: 22px;
    border-left-width: 11px;
  }
}

@media (max-width: 520px) {
  .breadcrumbs a {
    padding: 5px;
  }
  .breadcrumbs a:before,
  .breadcrumbs a:after {
    border-top-width: 16px;
    border-bottom-width: 16px;
    border-left-width: 8px;
  }
  .breadcrumbs li a span:first-child {
    display: block;
    margin: 0 auto;
  }
  .breadcrumbs li a span:last-child {
    display: none;
  }
}