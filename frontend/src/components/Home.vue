<script setup lang="ts">

</script>

<template>
    <div>
        <section class="bg-primary" id="one">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 col-lg-offset-3 col-md-8 col-md-offset-2 text-center">
                        <h2 class="margin-top-0 text-white">Aplicação de Fretes</h2>
                        <br>
                        <p class="text-faded">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam faucibus metus ac pharetra feugiat. Maecenas et mauris dui. Nullam id ultrices libero. Nullam quis eros sed mi pretium interdum. Suspendisse non leo non sapien sollicitudin tincidunt. Sed id nulla ut nisi mollis convallis. Aenean condimentum massa orci, a mattis leo eleifend a. Nullam pharetra feugiat ex. Suspendisse pellentesque diam erat, sed suscipit lectus interdum sed. Quisque porttitor tellus sed erat ultricies, eget condimentum mauris viverra. Proin at faucibus nulla. Pellentesque tortor nulla, auctor eget pretium in, maximus ut elit. Integer venenatis nibh ante, vel elementum est tempor nec. Donec finibus felis felis, sed congue augue viverra a.
                        </p>
                        <a href="#moreabout" class="btn btn-default btn-xl page-scroll">Saiba Mais</a>
                    </div>
                    <div class="col-lg-6 col-lg-offset-3 col-md-8 col-md-offset-2 text-center">
                        
                    </div>
                </div>
            </div>
        </section>
        <section id="moreabout" class="margin-top-5">
            <div class="container-fluid">
                <h2 class="margin-top-0 text-center"> Solicite seu frete aqui </h2>
                <div class="text-container margin-top-3">
                    <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus</p>
                    <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>
                </div>
            </div>
        </section>
   </div>
</template>

<style scoped>

h1,h2,h3,h4,h5,h6 {
    font-family: 'Questrial','Helvetica Neue',Arial,sans-serif;
}

p {
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 20px;
}

.text-faded {
    color: rgba(245,245,245,0.7);
}

section {
    padding: 70px 0;
    border-radius: 15px;
}


.no-padding {
    padding: 0;
}
 
header .header-content {
    position: relative;
    width: 100%;
    padding: 100px 15px;
    text-align: center;
    z-index: 2;
}

header .header-content .inner h1 {
    margin-top: 0;
    margin-bottom: 0;
}

header .header-content .inner p {
    margin-bottom: 50px;
    font-size: 16px;
    font-weight: 300;
    color: rgba(255,255,255,0.7);
}

#video-background {
  position: absolute;
  right: 0; 
  bottom: 0;
  min-width: 100%; 
  min-height: 100%;
  width: auto; 
  height: auto;
  z-index: 1;
}

#video-background.collapsing {
  display:none;
}

footer {
    background-color:#2d2d2d;
}

@media(min-width:768px) {
    .icon-lg {
        font-size: 80px;
    }
    
    header {
        min-height: 100%;
    }

    header .header-content {
        position: absolute;
        top: 50%;
        padding: 0 50px;
        -webkit-transform: translateY(-50%);
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
    }

    header .header-content .inner {
        margin-right: auto;
        margin-left: auto;
        max-width: 1000px;
    }

    header .header-content .inner h1 {
        font-size: 53px;
    }

    header .header-content .inner p {
        margin-right: auto;
        margin-left: auto;
        max-width: 80%;
        font-size: 18px;
    }
    
    section {
        min-height: 600px;
        padding: 100px 0;
    }

}

.form-control {
    display: block;
    width: 100%;
    height: 35px;
    padding: 6px 12px;
    font-size: 14px;
    line-height: 1.5;
    color: #eee;
    background-color: #36333d;
    background-image: none;
    border: 1px solid #36333d;
    border-radius: 4px;
    box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
    transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}

.form-control:focus {
    color: #222;
    background-color: #ccc;
    box-shadow: none;
}

textarea {
    resize: none;
}

.margin-top-0 {
    margin-top: 0;
}

.feature {
    margin: 50px auto 0;
    max-width: 400px;
}

@media(min-width:992px) {
    .feature {
        margin: 20px auto 0;
    }
}

.feature p {
    margin-bottom: 0;
}

.call-to-action h2 {
    margin: 0 auto 20px;
}

.gallery-box {
    display: block;
    position: relative;
    margin: 0 auto;
    max-width: 650px;
    overflow:hidden;
}

.gallery-box .gallery-box-caption {
    display: block;
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 100%;
    text-align: center;
    color: #fff;
    opacity: 0;
    background: rgba(44,44,44,.8);
    -webkit-transition: all .35s;
    -moz-transition: all .35s;
    transition: all .35s;
}

.gallery-box .gallery-box-caption .gallery-box-content {
    position: absolute;
    top: 50%;
    width: 100%;
    text-align: center;
    transform: translateY(-50%);
}

.gallery-box:hover .gallery-box-caption {
    opacity: 1;
}

.gallery-box:hover img {
    -webkit-transform: scale(1.1);
    -ms-transform: scale(1.1);
    transform: scale(1.1);
}

.gallery-box img {
    -webkit-transition: all 300ms ease-in-out;
    transition: all 300ms ease-in-out;
}

.no-gutter > [class*=col-] {
    padding-right: 0;
    padding-left: 0;
}

.btn-default {
    border-color: #fff;
    color: #222;
    background-color: #fff;
    -webkit-transition: all .35s;
    -moz-transition: all .35s;
    transition: all .35s;
}

.btn-default:hover,
.btn-default:focus,
.btn-default.focus,
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
    border-color: #ededed;
    color: #222;
    background-color: #f2f2f2;
    opacity: 0.7;
}

.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
    background-image: none;
}

.btn-default.disabled,
.btn-default[disabled],
fieldset[disabled] .btn-default,
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus,
.btn-default.disabled:active,
.btn-default[disabled]:active,
fieldset[disabled] .btn-default:active,
.btn-default.disabled.active,
.btn-default[disabled].active,
fieldset[disabled] .btn-default.active {
    border-color: #fff;
    background-color: #fff;
    opacity: 0.7;
}

.btn-default .badge {
    color: #fff;
    background-color: #222;
}

.btn.btn-primary {
    background-color: transparent;
    border:1px solid #f0f0f0;
    border-color:#f0f0f0;
    -webkit-transition: all .35s;
    -moz-transition: all .35s;
    transition: all .35s;
}

.btn.btn-primary:hover {
    opacity: 0.7;
}

.btn {
    border: 0;
    border-radius: 290px;
    font-family: 'Helvetica Neue',Arial,sans-serif;
}

.btn-xl {
    padding: 15px 30px;
    font-size: 20px;
}

::-moz-selection {
    text-shadow: none;
    color: #fff;
    background: #222;
}

::selection {
    text-shadow: none;
    color: #fff;
    background: #222;
}

img::selection {
    color: #fff;
    background: 0 0;
}

img::-moz-selection {
    color: #fff;
    background: 0 0;
}
</style>