import json
import os
import time, datetime
import random
import requests,re
from bs4 import BeautifulSoup

# reseposne = requests.get(r"https://yxxq3.cc/play/3383-1-19.html")
#
# restxt = reseposne.text
#
# print(restxt)

# os.system("cd D:/Webcrawlers & start D:/Webcrawlers/fix.exe")

#
# 1. 排名    <div class="list_num red">2.</div>
# 2. 图片地址
# 3. 书名
# 4. 推荐指数
# 5. 作者
# 6. 五星评分
# 7. 价格



html = r'''

<html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<meta name="keywords" content="小说畅销榜,近30日畅销书排行榜,畅销图书排行榜">
<meta name="description" content="当当网小说畅销榜，近30日畅销书排行榜，为您提供真实、权威、可信的小说排行榜数据，查看畅销小说排行榜，就上DangDang.COM。">

<title>小说畅销榜-近30日畅销书排行榜-当当畅销图书排行榜</title>
    <script type="text/javascript" src="/books/js/jquery-1.4.2.min.js"></script>
    <script type="text/javascript" src="/books/js/common.js"></script>
    <script type="text/javascript" src="/books/js/popwin.js"></script><style data-id="immersive-translate-input-injected-css">.immersive-translate-input {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  z-index: 2147483647;
  display: flex;
  justify-content: center;
  align-items: center;
}
.immersive-translate-attach-loading::after {
  content: " ";

  --loading-color: #f78fb6;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  display: block;
  margin: 12px auto;
  position: relative;
  color: white;
  left: -100px;
  box-sizing: border-box;
  animation: immersiveTranslateShadowRolling 1.5s linear infinite;

  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-2000%, -50%);
  z-index: 100;
}

.immersive-translate-loading-spinner {
  vertical-align: middle !important;
  width: 10px !important;
  height: 10px !important;
  display: inline-block !important;
  margin: 0 4px !important;
  border: 2px rgba(221, 244, 255, 0.6) solid !important;
  border-top: 2px rgba(0, 0, 0, 0.375) solid !important;
  border-left: 2px rgba(0, 0, 0, 0.375) solid !important;
  border-radius: 50% !important;
  padding: 0 !important;
  -webkit-animation: immersive-translate-loading-animation 0.6s infinite linear !important;
  animation: immersive-translate-loading-animation 0.6s infinite linear !important;
}

@-webkit-keyframes immersive-translate-loading-animation {
  from {
    -webkit-transform: rotate(0deg);
  }

  to {
    -webkit-transform: rotate(359deg);
  }
}

@keyframes immersive-translate-loading-animation {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(359deg);
  }
}

.immersive-translate-input-loading {
  --loading-color: #f78fb6;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  display: block;
  margin: 12px auto;
  position: relative;
  color: white;
  left: -100px;
  box-sizing: border-box;
  animation: immersiveTranslateShadowRolling 1.5s linear infinite;
}

@keyframes immersiveTranslateShadowRolling {
  0% {
    box-shadow: 0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0),
      0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);
  }

  12% {
    box-shadow: 100px 0 var(--loading-color), 0px 0 rgba(255, 255, 255, 0),
      0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);
  }

  25% {
    box-shadow: 110px 0 var(--loading-color), 100px 0 var(--loading-color),
      0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);
  }

  36% {
    box-shadow: 120px 0 var(--loading-color), 110px 0 var(--loading-color),
      100px 0 var(--loading-color), 0px 0 rgba(255, 255, 255, 0);
  }

  50% {
    box-shadow: 130px 0 var(--loading-color), 120px 0 var(--loading-color),
      110px 0 var(--loading-color), 100px 0 var(--loading-color);
  }

  62% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 130px 0 var(--loading-color),
      120px 0 var(--loading-color), 110px 0 var(--loading-color);
  }

  75% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0),
      130px 0 var(--loading-color), 120px 0 var(--loading-color);
  }

  87% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0),
      200px 0 rgba(255, 255, 255, 0), 130px 0 var(--loading-color);
  }

  100% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0),
      200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0);
  }
}

.immersive-translate-modal {
  position: fixed;
  z-index: 2147483647;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
  font-size: 15px;
}

.immersive-translate-modal-content {
  background-color: #fefefe;
  margin: 10% auto;
  padding: 40px 24px 24px;
  border-radius: 12px;
  width: 350px;
  font-family: system-ui, -apple-system, "Segoe UI", "Roboto", "Ubuntu",
    "Cantarell", "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  position: relative;
}

@media screen and (max-width: 768px) {
  .immersive-translate-modal-content {
    margin: 25% auto !important;
  }
}

@media screen and (max-width: 480px) {
  .immersive-translate-modal-content {
    width: 80vw !important;
    margin: 20vh auto !important;
    padding: 20px 12px 12px !important;
  }

  .immersive-translate-modal-title {
    font-size: 14px !important;
  }

  .immersive-translate-modal-body {
    font-size: 13px !important;
    max-height: 60vh !important;
  }

  .immersive-translate-btn {
    font-size: 13px !important;
    padding: 8px 16px !important;
    margin: 0 4px !important;
  }

  .immersive-translate-modal-footer {
    gap: 6px !important;
    margin-top: 16px !important;
  }
}

.immersive-translate-modal .immersive-translate-modal-content-in-input {
  max-width: 500px;
}
.immersive-translate-modal-content-in-input .immersive-translate-modal-body {
  text-align: left;
  max-height: unset;
}

.immersive-translate-modal-title {
  text-align: center;
  font-size: 16px;
  font-weight: 700;
  color: #333333;
}

.immersive-translate-modal-body {
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  color: #333333;
  margin-top: 24px;
}

@media screen and (max-width: 768px) {
  .immersive-translate-modal-body {
    max-height: 250px;
    overflow-y: auto;
  }
}

.immersive-translate-close {
  color: #666666;
  position: absolute;
  right: 16px;
  top: 16px;
  font-size: 20px;
  font-weight: bold;
}

.immersive-translate-close:hover,
.immersive-translate-close:focus {
  text-decoration: none;
  cursor: pointer;
}

.immersive-translate-modal-footer {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 24px;
}

.immersive-translate-btn {
  width: fit-content;
  color: #fff;
  background-color: #ea4c89;
  border: none;
  font-size: 14px;
  margin: 0 8px;
  padding: 9px 30px;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.immersive-translate-btn-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.immersive-translate-btn:hover {
  background-color: #f082ac;
}
.immersive-translate-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.immersive-translate-btn:disabled:hover {
  background-color: #ea4c89;
}

.immersive-translate-link-btn {
  background-color: transparent;
  color: #ea4c89;
  border: none;
  cursor: pointer;
  height: 30px;
  line-height: 30px;
}

.immersive-translate-cancel-btn {
  /* gray color */
  background-color: rgb(89, 107, 120);
}

.immersive-translate-cancel-btn:hover {
  background-color: hsl(205, 20%, 32%);
}

.immersive-translate-action-btn {
  background-color: transparent;
  color: #ea4c89;
  border: 1px solid #ea4c89;
}

.immersive-translate-btn svg {
  margin-right: 5px;
}

.immersive-translate-link {
  cursor: pointer;
  user-select: none;
  -webkit-user-drag: none;
  text-decoration: none;
  color: #ea4c89;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0.1);
}

.immersive-translate-primary-link {
  cursor: pointer;
  user-select: none;
  -webkit-user-drag: none;
  text-decoration: none;
  color: #ea4c89;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0.1);
}

.immersive-translate-modal input[type="radio"] {
  margin: 0 6px;
  cursor: pointer;
}

.immersive-translate-modal label {
  cursor: pointer;
}

.immersive-translate-close-action {
  position: absolute;
  top: 2px;
  right: 0px;
  cursor: pointer;
}

.imt-image-status {
  background-color: rgba(0, 0, 0, 0.5) !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 16px !important;
}
.imt-image-status img,
.imt-image-status svg,
.imt-img-loading {
  width: 28px !important;
  height: 28px !important;
  margin: 0 0 8px 0 !important;
  min-height: 28px !important;
  min-width: 28px !important;
  position: relative !important;
}
.imt-img-loading {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADgAAAA4CAMAAACfWMssAAAAtFBMVEUAAAD////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////oK74hAAAAPHRSTlMABBMIDyQXHwyBfFdDMSw+OjXCb+5RG51IvV/k0rOqlGRM6KKMhdvNyZBz9MaupmxpWyj437iYd/yJVNZeuUC7AAACt0lEQVRIx53T2XKiUBCA4QYOiyCbiAsuuGBcYtxiYtT3f6/pbqoYHVFO5r+iivpo6DpAWYpqeoFfr9f90DsYAuRSWkFnPO50OgR9PwiCUFcl2GEcx+N/YBh6pvKaefHlUgZd1zVe0NbYcQjGBfzrPE8Xz8aF+71D8gG6DHFPpc4a7xFiCDuhaWgKgGIJQ3d5IMGDrpS4S5KgpIm+en9f6PlAhKby4JwEIxlYJV9h5k5nee9GoxHJ2IDSNB0dwdad1NAxDJ/uXDHYmebdk4PdbkS58CIVHdYSUHTYYRWOJblWSyu2lmy3KNFVJNBhxcuGW4YBVCbYGRZwIooipHsNqjM4FbgOQqQqSKQQU9V8xmi1QlgHqQQ6DDBvRUVCDirs+EzGDGOQTCATgtYTnbCVLgsVgRE0T1QE0qHCFAht2z6dLvJQs3Lo2FQoDxWNUiBhaP4eRgwNkI+dAjVOA/kUrIDwf3CG8NfNOE0eiFotSuo+rBiq8tD9oY4Qzc6YJw99hl1wzpQvD7ef2M8QgnOGJfJw+EltQc+oX2yn907QB22WZcvlUpd143dqQu+8pCJZuGE4xCuPXJqqcs5sNpsI93Rmzym1k4Npk+oD1SH3/a3LOK/JpUBpWfqNySxWzCfNCUITuDG5dtuphrUJ1myeIE9bIsPiKrfqTai5WZxbhtNphYx6GEIHihyGFTI69lje/rxajdh0s0msZ0zYxyPLhYCb1CyHm9Qsd2H37Y3lugVwL9kNh8Ot8cha6fUNQ8nuXi5z9/ExsAO4zQrb/ev1yrCB7lGyQzgYDGuxq1toDN/JGvN+HyWNHKB7zEoK+PX11e12G431erGYzwmytAWU56fkMHY5JJnDRR2eZji3AwtIcrEV8Cojat/BdQ7XOwGV1e1hDjGGjXbdArm8uJZtCH5MbcctVX8A1WpqumJHwckAAAAASUVORK5CYII=");
  background-size: 28px 28px;
  animation: image-loading-rotate 1s linear infinite !important;
}

.imt-image-status span {
  color: var(--bg-2, #fff) !important;
  font-size: 14px !important;
  line-height: 14px !important;
  font-weight: 500 !important;
  font-family: "PingFang SC", Arial, sans-serif !important;
}

.imt-primary-button {
  display: flex;
  padding: 12px 80px;
  justify-content: center;
  align-items: center;
  gap: 8px;
  border-radius: 8px;
  background: #ea4c89;
  color: #fff;
  font-size: 16px;
  font-style: normal;
  font-weight: 700;
  line-height: 24px;
  border: none;
  cursor: pointer;
}

.imt-retry-text {
  color: #999;
  text-align: center;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 21px;
  cursor: pointer;
}

.imt-action-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.imt-modal-content-text {
  text-align: left;
  color: #333;
  font-size: 16px;
  font-weight: 400;
  line-height: 24px;
}

@keyframes image-loading-rotate {
  from {
    transform: rotate(360deg);
  }
  to {
    transform: rotate(0deg);
  }
}

.imt-linear-gradient-text {
  background: linear-gradient(90deg, #00a6ff 0%, #c369ff 52.4%, #ff4590 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.imt-flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.imt-linear-black-btn {
  border-radius: 50px;
  background: linear-gradient(66deg, #222 19%, #696969 94.25%);
  height: 48px;
  width: 100%;
  color: #fff;
  font-size: 16px;
  font-weight: 700;
  display: flex;
  align-items: center;
  cursor: pointer;
  justify-content: center;
}
</style></head><body><div id="popwin" style="position:absolute; padding:0; margin:0;" onmouseover="clearTimeout(window.hideTimeout);clearTimeout(window.keepTimeout)" onmouseout="popwin.hide()"></div>
    <script type="text/javascript" src="http://static.ddimg.cn/js/login/LoginWindow.js"></script><link href="//static.dangdang.com/css/win_login20150728.css?20170215" rel="stylesheet" type="text/css">
    <link type="text/css" href="/books/css/bang_list.css" rel="stylesheet">
    <script type="text/javascript" src="/books/js/DD_belatedPNG_0.0.8a.js"></script>
    <script type="text/javascript">
    DD_belatedPNG.fix('.level,.level span');
    </script> 
    <script type="text/javascript" src="http://a.dangdang.com/smart.js"></script>


    
    <!-- 页头 begin -->
    <script>var accessbilityUrl = "//static.dangdang.com/fed/accessbility/1.0.0/accessbility.min.js";var accessbilitySwitch = "1";</script>
<script type="text/javascript" defer="" async="" src="//static.dangdang.com/js/header2012/pagetop_accessbility.min.js?v=20230626"></script><script type="text/javascript">
    </script>
<script type="text/javascript">
function is_narrow(){
    var datanav="";
    if(screen.width < 1210){
       datanav='<li ><a name="nav1" href="https://book.dangdang.com/" target="_blank">图书</a></li><li ><a name="nav1" href="https://category.dangdang.com/cp01.82.00.00.html" target="_blank">特装书</a></li><li ><a name="nav1" href="https://category.dangdang.com/cp01.83.00.00.html" target="_blank">亲签书</a></li><li ><a name="nav1" href="http://e.dangdang.com/index_page.html" target="_blank">电子书</a></li><li ><a name="nav1" href="https://category.dangdang.com/cp01.76.00.00.html" target="_blank">课程</a></li><li ><a name="nav1" href="https://shop.dangdang.com/25161" target="_blank">正版教材</a></li><li ><a name="nav1" href="https://book.dangdang.com/20251009_guof" target="_blank">特色书城</a></li><li ><a name="nav1" href="http://category.dangdang.com/cid4004344.html" target="_blank">童装童鞋</a></li><li ><a name="nav1" href="https://product.dangdang.com/29980423.html" target="_blank">地下王朝</a><span class="icon_n"><img src="https://platform-permanent.ddimg.cn/pt-front-cms-upload-file/2026/1/5/2026010510452716634.png" alt="" /></span></li>';
    }else{
    datanav='<li ><a name="nav1" href="https://book.dangdang.com/" target="_blank">图书</a></li><li ><a name="nav1" href="https://category.dangdang.com/cp01.82.00.00.html" target="_blank">特装书</a></li><li ><a name="nav1" href="https://category.dangdang.com/cp01.83.00.00.html" target="_blank">亲签书</a></li><li ><a name="nav1" href="http://e.dangdang.com/index_page.html" target="_blank">电子书</a></li><li ><a name="nav1" href="https://category.dangdang.com/cp01.76.00.00.html" target="_blank">课程</a></li><li ><a name="nav1" href="https://shop.dangdang.com/25161" target="_blank">正版教材</a></li><li ><a name="nav1" href="https://book.dangdang.com/20251009_guof" target="_blank">特色书城</a></li><li ><a name="nav1" href="http://category.dangdang.com/cid4004344.html" target="_blank">童装童鞋</a></li><li ><a name="nav1" href="https://product.dangdang.com/29980423.html" target="_blank">地下王朝</a><span class="icon_n"><img src="https://platform-permanent.ddimg.cn/pt-front-cms-upload-file/2026/1/5/2026010510452716634.png" alt="" /></span></li>';
    }
    return datanav;
}
</script>
<link href="//static.dangdang.com/css/header2012/header_150803.css?20251111" rel="stylesheet" type="text/css">
<script charset="gb2312" type="text/javascript">var width = 1; narrow = 0;</script>
<script src="//static.dangdang.com/js/header2012/pagetop2015_0827.js?20251111" charset="gb2312" type="text/javascript"></script>
<script src="//static.dangdang.com/js/header2012/dd.menu-aim.js?20251111" charset="gb2312" type="text/javascript"></script>


<div id="hd">
<div id="tools">
<div class="tools">
<style>.ddnewhead_operate_nav img {display: inline;}</style>
<div class="ddnewhead_operate" dd_name="顶链接">
  <div style="float:right">
    <div class="new_head_znx" id="znx_content" style="display:none;float:left"></div>
    <div class="ddnewhead_welcome" display="none;" style="float:left">
      <span id="nickname">欢迎光临当当，请<a dd_name="登录" href="javascript:PageTopLogIn();" target="_self" rel="nofollow" class="login_link">登录</a><a dd_name="成为会员" href="javascript:PageTopRegist();" target="_self" rel="nofollw">成为会员</a></span>
      <div class="tel_pop" style="display:none" id="__ddnav_sjdd" onmouseover="showgaoji('a_phonechannel','__ddnav_sjdd');" onmouseout="hideotherchannel('a_phonechannel','__ddnav_sjdd');">
        <a target="_blank" href="http://t.dangdang.com/20130220_ydmr" class="title"><i class="icon_tel"></i>手机当当</a><i class="title_shadow"></i>
        <ul class="tel_pop_box">
          <li><a href="http://t.dangdang.com/20130220_ydmr" dd_name="手机二维码"><span>当当手机客户端</span><img src="//img3.ddimg.cn/00363/doc/erweima2.png"><span class="text">随手查订单<br>随时享优惠</span></a></li>
        </ul>
      </div>
    </div>
<ul class="ddnewhead_operate_nav" style="float:left"><li class="ddnewhead_cart"><a href="javascript:AddToShoppingCart(0);" name="购物车" dd_name="购物车">
<img src="https://platform-permanent.ddimg.cn/pt-front-cms-upload-file/2025/12/19/2025121912002032910.png" style="width: 15px;height: 14px;margin-right: 4px;position: relative;top: 2px;">
购物车<b id="cart_items_count">0</b></a></li><li class="wddd0"><a target="_blank" href="http://myhome.dangdang.com/myOrder" name="我的订单" dd_name="我的订单" id="a_wddd0channel">我的订单</a>


</li><li class="wdysf1"><a target="_blank" href="http://e.dangdang.com/booksshelf_page.html" name="我的云书房" dd_name="我的云书房" id="a_wdysf1channel">我的云书房</a>


</li><li class="wddd2"><a class="menu_btn" target="_blank" href="http://myhome.dangdang.com/" name="我的当当" dd_name="我的当当" id="a_wddd2channel" onmouseover="showgaoji('a_wddd2channel','__ddnav_wddd2')" onmouseout="hideotherchannel('a_wddd2channel','__ddnav_wddd2');">我的当当</a>

    <ul class="ddnewhead_gcard_list" id="__ddnav_wddd2" onmouseover="showgaoji('a_wddd2channel','__ddnav_wddd2')" onmouseout="hideotherchannel('a_wddd2channel','__ddnav_wddd2');"><li>
    <a target="_blank" href="http://myhome.dangdang.com/mypoint?ref=my-0-L" name="mydd_4" dd_name="银铃铛抵现" rel="nofollow">银铃铛抵现</a>
</li><li>
    <a target="_blank" href="http://myhome.dangdang.com/myFavorite" name="mydd_4" dd_name="我的收藏" rel="nofollow">我的收藏</a>
</li><li>
    <a target="_blank" href="http://noncash.dangdang.com/balance/" name="mydd_4" dd_name="我的余额" rel="nofollow">我的余额</a>
</li><li>
    <a target="_blank" href="http://comment.dangdang.com/comment" name="mydd_4" dd_name="我的评论" rel="nofollow">我的评论</a>
</li><li>
    <a target="_blank" href="http://newaccount.dangdang.com/payhistory/mycoupon.aspx" name="mydd_4" dd_name="礼券/礼品卡" rel="nofollow">礼券/礼品卡</a>
</li> </ul>

</li><li class="ddpt3"><a target="_blank" href="http://t.dangdang.com/pintuan_list" name="当当拼团" dd_name="当当拼团" id="a_ddpt3channel">当当拼团</a>


</li><li class="qycg4"><a class="menu_btn" target="_blank" href="http://giftcard.dangdang.com/" name="企业采购" dd_name="企业采购" id="a_qycg4channel" onmouseover="showgaoji('a_qycg4channel','__ddnav_qycg4')" onmouseout="hideotherchannel('a_qycg4channel','__ddnav_qycg4');">企业采购</a>

    <ul class="ddnewhead_gcard_list" id="__ddnav_qycg4" onmouseover="showgaoji('a_qycg4channel','__ddnav_qycg4')" onmouseout="hideotherchannel('a_qycg4channel','__ddnav_qycg4');"><li>
    <a target="_blank" href="http://b2b.dangdang.com/ddRegistered?custId=2c21d394a078586625dec5580df4f63f&amp;sid=pc_8b1ba6ca9befd77f806ba23c7fed310a7c001a089742c9a5d1c9bf27c1bf1c98" name="mydd_4" dd_name="企业/馆配" rel="nofollow">企业/馆配</a>
</li><li>
    <a target="_blank" href="http://giftcard.dangdang.com/" name="mydd_4" dd_name="礼品卡采购" rel="nofollow">礼品卡采购</a>
</li><li>
    <a target="_blank" href="http://newaccount.dangdang.com/payhistory/mymoney.aspx" name="mydd_4" dd_name="礼品卡激活" rel="nofollow">礼品卡激活</a>
</li><li>
    <a target="_blank" href="http://help.dangdang.com/details/page24" name="mydd_4" dd_name="礼品卡使用" rel="nofollow">礼品卡使用</a>
</li><li>
    <a target="_blank" href="http://b2b.dangdang.com/" name="mydd_4" dd_name="分销/荐购" rel="nofollow">分销/荐购</a>
</li><li>
    <a target="_blank" href="http://giftcard.dangdang.com/goods?type=mall" name="mydd_4" dd_name="礼品卡专区" rel="nofollow">礼品卡专区</a>
</li> </ul>

</li><li class="khfw5"><a class="menu_btn" target="_blank" href="http://help.dangdang.com/index" name="客户服务" dd_name="客户服务" id="a_khfw5channel" onmouseover="showgaoji('a_khfw5channel','__ddnav_khfw5')" onmouseout="hideotherchannel('a_khfw5channel','__ddnav_khfw5');">客户服务</a>

    <ul class="ddnewhead_gcard_list" id="__ddnav_khfw5" onmouseover="showgaoji('a_khfw5channel','__ddnav_khfw5')" onmouseout="hideotherchannel('a_khfw5channel','__ddnav_khfw5');"><li>
    <a target="_blank" href="http://help.dangdang.com/index" name="mydd_4" dd_name="帮助中心" rel="nofollow">帮助中心</a>
</li><li>
    <a target="_blank" href="http://return.dangdang.com/reverseapplyselect.aspx" name="mydd_4" dd_name="自助退换货" rel="nofollow">自助退换货</a>
</li><li>
    <a target="_blank" href="http://order.dangdang.com/InvoiceApply/InvoiceOnlineReissue.aspx" name="mydd_4" dd_name="自助发票" rel="nofollow">自助发票</a>
</li><li>
    <a target="_blank" href="http://help.dangdang.com/details/page206" name="mydd_4" dd_name="联系客服" rel="nofollow">联系客服</a>
</li><li>
    <a target="_blank" href="http://help.dangdang.com/details/page206" name="mydd_4" dd_name="我要投诉" rel="nofollow">我要投诉</a>
</li> </ul>

</li><li class="dd_assist_btn_id" id="dd_assist_btn_id" style="cursor: pointer;"><a alt="点击切换至无障碍" dd_name="切换无障碍" name="切换无障碍" href="javascript:void(0);">切换无障碍</a></li></ul>
      </div>
    </div>
  </div>
</div>
<div id="header_end"></div>
<!--CreateDate  2026-01-05 15:00:01--><div style="position:relative;" class="logo_line_out" ddaccregion="mutual">
<div class="logo_line" dd_name="搜索框">
    <div class="logo"><img src="https://platform-permanent.ddimg.cn/pt-front-cms-upload-file/2025/12/18/2025121814464873534.png" usemap="#logo_link">
                         <map name="logo_link" id="logo_link" dd_name="logo区"><area shape="rect" coords="0,18,200,93" href="http://www.dangdang.com" title="当当" onfocus="this.blur();" tabindex="-1">
                         <area shape="rect" coords="200,18,320,93" href="http://www.dangdang.com/" title="当当" target="_blank" onfocus="this.blur();" tabindex="-1"></map></div>
    <div class="search">
        <form action="//search.dangdang.com" name="searchform" id="form_search_new" onsubmit="return searchsubmit();" method="GET">
            <label for="key_S" class="label_search" id="label_key" onclick="this.style.color='rgb(255, 255, 255)';" style="visibility: visible; color: rgb(102, 102, 102);">地下王朝 特装版</label>
            <input type="text" class="text gray" name="key" id="key_S" autocomplete="off" onclick="key_onclick(event);" onfocus="key_onfocus(event);" onblur="key_onblur();" onbeforepaste="onpaste_search();"><a href="javascript:void(0);" onclick="clearkeys();" class="del-keywords" tabindex="-1"></a><span class="select" onmouseover="allCategoryShow();" onmouseleave="allCategoryHide();" onmouseout="if(&quot;\v&quot;!=&quot;v&quot;){ allCategoryHide();}"><span id="Show_Category_Name" dd_name="全部分类">全部分类</span><span class="icon"></span>
                <div id="search_all_category" class="select_pop" style="height:0px;padding: 0px;border-width: 0px;" dd_name="搜索分类">
                    <a href="javascript:void(0);" onclick="selectCategory('',this);"><span id="Show_Category_Name" dd_name="全部分类" tabindex="-1">全部分类</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory('100000',this);" dd_name="尾品汇"><span>尾品汇</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory('01.00.00.00.00.00',this);" dd_name="图书"><span>图书</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory('98.00.00.00.00.00',this);" dd_name="电子书"><span>电子书</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory('03.00.00.00.00.00',this);" dd_name="音像"><span>音像</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory('05.00.00.00.00.00',this);" dd_name="影视"><span>影视</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4002074,this);" dd_name="时尚美妆"><span>时尚美妆</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4001940,this);" dd_name="母婴用品"><span>母婴用品</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4002061,this);" dd_name="玩具"><span>玩具</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4004866,this);" dd_name="孕婴服饰"><span>孕婴服饰</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4004344,this);" dd_name="童装童鞋"><span>童装童鞋</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4003900,this);" dd_name="家居日用"><span>家居日用</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4003760,this);" dd_name="家具装饰"><span>家具装饰</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4003844,this);" dd_name="服装"><span>服装</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4003872,this);" dd_name="鞋"><span>鞋</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4001829,this);" dd_name="箱包皮具"><span>箱包皮具</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4003639,this);" dd_name="手表饰品"><span>手表饰品</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4003728,this);" dd_name="运动户外"><span>运动户外</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4002429,this);" dd_name="汽车用品"><span>汽车用品</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4002145,this);" dd_name="食品"><span>食品</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4006497,this);" dd_name="手机通讯"><span>手机通讯</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4003613,this);" dd_name="数码影音"><span>数码影音</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4003819,this);" dd_name="电脑办公"><span>电脑办公</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4007241,this);" dd_name="大家电"><span>大家电</span></a>
                                        <a href="javascript:void(0);" onclick="selectCategory(4001001,this);" dd_name="家用电器"><span>家用电器</span></a>
                                    </div>
            </span>
            <input type="hidden" id="default_key" value="地下王朝 特装版">
            <input type="hidden" id="default_key_link" value="https://search.dangdang.com/?key=%B5%D8%CF%C2%CD%F5%B3%AF%20%CC%D8%D7%B0%B0%E6&amp;act=input" mid1_value="12" api_step="d">
            <input type="submit" id="search_btn" dd_name="搜索按钮" style="display:none">
            <input id="SearchFromTop" style="display:none" type="hidden" name="SearchFromTop" value="1">
            <input type="button" id="suggest_product_btn" name="suggestproduct_btn" style="display:none" onclick="void(0)">
            <input type="button" id="suggest_class_btn" name="suggestclass_btn" style="display:none" onclick="void(0)">
            <input type="submit" id="suggest_searchkey_btn" name="suggestsearchkey_btn" style="display:none" dd_name="搜索按钮">
            <input type="hidden" id="catalog_S" name="catalog" value="">
            <input type="button" class="button" dd_name="搜索按钮" onclick="javascript:document.getElementById('search_btn').click();">
        </form>
    </div>
    <div class="search_bottom">
        <div class="search_hot">热搜: <a href="https://search.dangdang.com/?key=%BC%D7%B9%C7%CE%C4%D1%A7%D0%A3%CF%B5%C1%D0&amp;act=input" name="hotword" target="_blank">甲骨文学校系列</a><a href="https://search.dangdang.com/?key=%D3%CE%CF%B7%C8%EB%C7%D6&amp;act=input" name="hotword" target="_blank">游戏入侵</a><a href="https://search.dangdang.com/?key=%CA%B1%BC%E4%BC%F2%CA%B7&amp;act=input" name="hotword" target="_blank">时间简史</a><a href="https://search.dangdang.com/?key=%D7%D4%CA%C9%C1%A6&amp;act=input" name="hotword" target="_blank">自噬力</a><a href="https://search.dangdang.com/?key=%C6%B6%C7%EE%B5%C4%B1%BE%D6%CA&amp;act=input" name="hotword" target="_blank">贫穷的本质</a><a href="https://book.dangdang.com/20220907_3d2t" name="hotword" target="_blank">9.9元包邮</a></div>
        <a href="http://search.dangdang.com/advsearch" class="search_advs" target="_blank" name="ddnav_adv_s" dd_name="高级搜索">高级搜索</a>
    </div>
    <div id="suggest_key" class="suggest_key" style="display:none;"></div>
    <div class="ddnew_cart"><a href="javascript:AddToShoppingCart(0);" name="购物车" dd_name="购物车"><i class="icon_card"></i>购物车<b id="cart_items_count"></b></a></div>
    <div class="ddnew_order"><a target="_blank" href="http://myhome.dangdang.com/myOrder" name="我的订单" dd_name="我的订单" rel="nofollow">我的订单<b id="unpaid_num" style="color:#ff2832;font:bold 12px Arial;"></b></a></div>
</div>
</div><div class="nav_top" dd_name="一级导航条">
<div class="nav_top">
    <ul>
        <li class="all"><a href="http://category.dangdang.com/?ref=www-0-C" id="a_category" name="cate" class="sort_button" onmouseover="showCategory('a_category','__ddnav_sort','//static.dangdang.com/js/header2012/categorydata_new.js?20251111');" onmouseout="closeCategory('__ddnav_sort');" dd_name="全部商品分类" target="_blank">全部商品分类</a></li>
        <script language="javascript">document.write(is_narrow());</script><li><a name="nav1" href="https://book.dangdang.com/" target="_blank">图书</a></li><li><a name="nav1" href="https://category.dangdang.com/cp01.82.00.00.html" target="_blank">特装书</a></li><li><a name="nav1" href="https://category.dangdang.com/cp01.83.00.00.html" target="_blank">亲签书</a></li><li><a name="nav1" href="http://e.dangdang.com/index_page.html" target="_blank">电子书</a></li><li><a name="nav1" href="https://category.dangdang.com/cp01.76.00.00.html" target="_blank">课程</a></li><li><a name="nav1" href="https://shop.dangdang.com/25161" target="_blank">正版教材</a></li><li><a name="nav1" href="https://book.dangdang.com/20251009_guof" target="_blank">特色书城</a></li><li><a name="nav1" href="http://category.dangdang.com/cid4004344.html" target="_blank">童装童鞋</a></li><li><a name="nav1" href="https://product.dangdang.com/29980423.html" target="_blank">地下王朝</a><span class="icon_n"><img src="https://platform-permanent.ddimg.cn/pt-front-cms-upload-file/2026/1/5/2026010510452716634.png" alt=""></span></li>
    </ul>
</div>
</div><div class="home_nav_l_box">
<div class="home_nav_l" id="nav_l" style="display:none;">

<div class="new_pub_nav_box" dd_name="左侧分类导航" style="display:none;" id="__ddnav_sort" onmouseover="showdiv(event,'__ddnav_sort');" onmouseout="hiddenCategory(event,'__ddnav_sort');">
    <span class="new_pub_line_a"></span>
    <span class="new_pub_line_b"></span>
    <div class="new_pub_nav_shadow" id="menu_list">
		<ul class="new_pub_nav" id="menulist_content">
            			<li class="n_b first" dd_name="图书童书" id="li_label_1" data-submenu-id="__ddnav_sort1" data_index="1" data_key="1000000" data_type="'goods'">
                <span class="nav" id="categoryh_1">
                    <a name="newcate1" dd_name="图书" id="cate_21091" href="https://book.dangdang.com/" target="_blank">图书</a>、<a name="newcate1" dd_name="童书" id="cate_21092" href="https://book.dangdang.com/children?ref=book-01-A" target="_blank">童书</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="电子书" id="li_label_2" data-submenu-id="__ddnav_sort2" data_index="2" data_key="1000001" data_type="'book'">
                <span class="nav" id="categoryh_2">
                    <a name="newcate2" dd_name="电子书" id="cate_21218" href="http://e.dangdang.com/index_page.html" target="_blank">电子书</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="创意文具" id="li_label_3" data-submenu-id="__ddnav_sort3" data_index="3" data_key="1000002" data_type="'goods'">
                <span class="nav" id="categoryh_3">
                    <a name="newcate3" dd_name="创意文具" id="cate_21288" href="https://search.dangdang.com/?key=%B4%B4%D2%E2%CE%C4%BE%DF&amp;act=input" target="_blank">创意文具</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="服饰内衣" id="li_label_4" data-submenu-id="__ddnav_sort4" data_index="4" data_key="1000003" data_type="'goods'">
                <span class="nav" id="categoryh_4">
                    <a name="newcate4" dd_name="服饰" id="cate_21392" href="http://category.dangdang.com/cid4003844.html" target="_blank">服饰</a>、<a name="newcate4" dd_name="内衣" id="cate_21393" href="http://category.dangdang.com/cid10010337.html" target="_blank">内衣</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="运动户外" id="li_label_5" data-submenu-id="__ddnav_sort5" data_index="5" data_key="1000004" data_type="'goods'">
                <span class="nav" id="categoryh_5">
                    <a name="newcate5" dd_name="运动户外" id="cate_21455" href="https://search.dangdang.com/?key=%D4%CB%B6%AF%BB%A7%CD%E2&amp;act=input&amp;category_id=4003728&amp;type=4003728" target="_blank">运动户外</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="孕婴童" id="li_label_6" data-submenu-id="__ddnav_sort6" data_index="6" data_key="1000005" data_type="'goods'">
                <span class="nav" id="categoryh_6">
                    <a name="newcate6" dd_name="孕" id="cate_21503" href="https://category.dangdang.com/cid4004866.html" target="_blank">孕</a>、<a name="newcate6" dd_name="婴" id="cate_21504" href="https://category.dangdang.com/cid4001940.html" target="_blank">婴</a>、<a name="newcate6" dd_name="童" id="cate_21505" href="https://category.dangdang.com/cid4004344.html" target="_blank">童</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="家居家纺" id="li_label_7" data-submenu-id="__ddnav_sort7" data_index="7" data_key="1000006" data_type="'goods'">
                <span class="nav" id="categoryh_7">
                    <a name="newcate7" dd_name="家居" id="cate_21559" href="https://search.dangdang.com/?key=%BC%D2%BE%D3&amp;act=input&amp;category_id=4003900&amp;type=4003900" target="_blank">家居</a>、<a name="newcate7" dd_name="家纺" id="cate_21560" href="https://search.dangdang.com/?key=%BC%D2%B7%C4&amp;act=input&amp;category_id=4003900&amp;type=4003900" target="_blank">家纺</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="家具家装" id="li_label_8" data-submenu-id="__ddnav_sort8" data_index="8" data_key="1000007" data_type="'goods'">
                <span class="nav" id="categoryh_8">
                    <a name="newcate8" dd_name="家具" id="cate_21613" href="http://category.dangdang.com/cid4004162.html" target="_blank">家具</a>、<a name="newcate8" dd_name="家装" id="cate_21614" href="http://category.dangdang.com/cid4009484.html" target="_blank">家装</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="食品茶酒" id="li_label_9" data-submenu-id="__ddnav_sort9" data_index="9" data_key="1000008" data_type="'goods'">
                <span class="nav" id="categoryh_9">
                    <a name="newcate9" dd_name="食品" id="cate_21678" href="https://search.dangdang.com/?key=%CA%B3%C6%B7&amp;act=input&amp;category_id=4002145&amp;type=4002145" target="_blank">食品</a>、<a name="newcate9" dd_name="茶酒" id="cate_21679" href="http://category.dangdang.com/cid4005722.html" target="_blank">茶酒</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="家用电器" id="li_label_10" data-submenu-id="__ddnav_sort10" data_index="10" data_key="1000009" data_type="'goods'">
                <span class="nav" id="categoryh_10">
                    <a name="newcate10" dd_name="家用电器" id="cate_21702" href="https://search.dangdang.com/?key=%BC%D2%D3%C3%B5%E7%C6%F7&amp;act=input&amp;category_id=4001001&amp;type=4001001" target="_blank">家用电器</a></span><span class="sign"></span>
            </li>
            			<li class="n_b" dd_name="当当礼品卡" id="li_label_11" data-submenu-id="__ddnav_sort11" data_index="11" data_key="1000010" data_type="'goods'">
                <span class="nav" id="categoryh_11">
                    <a name="newcate11" dd_name="当当礼品卡" id="cate_21741" href="http://giftcard.dangdang.com/" target="_blank">当当礼品卡</a></span><span class="sign"></span>
            </li>
            		</ul>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort1"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort2"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort3"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort4"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort5"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort6"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort7"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort8"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort9"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort10"></div>
                <div class="new_pub_nav_pop" style="display: none;" id="__ddnav_sort11"></div>
            </div>
</div>
</div></div>
<div class="sub">
    <ul>
                <li><a name="nav2" target="_blank" href="http://bang.dangdang.com/books/">图书排行榜</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/children">童书</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/study">中小学用书</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.03.htm">小说</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.05.htm">文学</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.01.htm">青春文学</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.07.htm">艺术</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.21.htm">成功励志</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.22.htm">管理</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.36.htm">历史</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.28.htm">哲学宗教</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.15.htm">亲子家教</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/01.18.htm">保健养生</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/exam?biaoti">考试</a></li>
                        <li><a name="nav2" target="_blank" href="https://book.dangdang.com/exam?biaoti">科技</a></li>
                        <li><a name="nav2" target="_blank" href="http://category.dangdang.com/cp01.58.00.00.00.00.html">进口原版</a></li>
                        <li><a name="nav2" target="_blank" href="http://e.dangdang.com/index_page.html">电子书</a></li>
                    </ul>
</div>
</div>
<script type="text/javascript">
var newsuggesturl = "//schprompt.dangdang.com/suggest_new.php?";
var nick_num = 1;
initHeaderOperate();Suggest_Initialize("key_S");
if(!window.onload){
    window.onload=function(){if(sug_gid("label_key").style.visibility=="visible")sug_gid(search_input_id).value="";}
}else{
    var funcload=window.onload;
    window.onload=function(){funcload();if(sug_gid("label_key").style.visibility=="visible")sug_gid(search_input_id).value="";}
}
ddmenuaim(document.getElementById("menulist_content"),{activate: activateSubmenu,deactivate: deactivateSubmenu});
</script>
<!--DOC-HEAD-END--><!-- 页头 end -->
    <div class="bang_wrapper">
        <div class="layout_location"><a href="http://www.dangdang.com">当当网</a><span class="path">&gt;</span>
            <a href="http://bang.dangdang.com/books/">图书榜</a>
        <span class="path">&gt;</span>
            <a href="http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1">图书畅销榜</a>
        <span class="path">&gt;</span>
        <span>小说</span> 
</div>        <!--bang_title-->
        <div class="bang_title">
    <div class="tab">
                <h2 class="now"><a href="http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1">图书畅销榜</a></h2>  
                <h2><a href="http://bang.dangdang.com/books/newhotsales/01.00.00.00.00.00-24hours-0-0-1-1">新书热卖榜</a></h2>  
                <h2><a href="http://bang.dangdang.com/books/childrensbooks/01.41.00.00.00.00-24hours-0-0-1-1">童书榜</a></h2>  
                <h2><a href="http://bang.dangdang.com/books/hotbang">热搜榜</a></h2>  
                <h2><a href="http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1">好评榜</a></h2>  
                <h2><a href="http://bang.dangdang.com/books/soaringsales/01.00.00.00.00.00-0-0-0-1-1">飙升榜</a></h2>  
                <h2><a href="http://bang.dangdang.com/books/surplusbooks/01.00.00.00.00.00-recent7-0-0-1-1">特价榜</a></h2>  
                <h2><a href="http://e.dangdang.com/rank_detail_page.html?listType=ddds_sale&amp;channelType=all&amp;timeDimension=2">电子书畅销榜</a></h2>  
                <h2><a href="http://e.dangdang.com/rank_detail_page.html?listType=ddds_new&amp;channelType=all&amp;payType=1&amp;timeDimension=2">电子书新书热卖榜</a></h2>  
            </div>
    <h1>图书畅销榜<span>TOP500</span></h1>
</div>        <div class="bang_content">
            <!--bang_nav_box-->
            <div class="bang_nav_box">
    <div class="bang_nav" id="sortRanking">
        <div class="side_title">分类排行</div>

                <div class="side_nav" category_path="01.41.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.41.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">童书</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.43.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.43.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">中小学用书</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav hover" category_path="01.03.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">小说</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail" style="display: block;">
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.30.00.00.00-recent30-0-0-1-1">中国当代小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.38.00.00.00-recent30-0-0-1-1">侦探/悬疑/推理小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.35.00.00.00-recent30-0-0-1-1">外国小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.56.00.00.00-recent30-0-0-1-1">世界名著</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.45.00.00.00-recent30-0-0-1-1">社会小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.41.00.00.00-recent30-0-0-1-1">科幻小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.33.00.00.00-recent30-0-0-1-1">四大名著</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.51.00.00.00-recent30-0-0-1-1">历史小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.55.00.00.00-recent30-0-0-1-1">小说作品集</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.50.00.00.00-recent30-0-0-1-1">官场小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.32.00.00.00-recent30-0-0-1-1">中国古典小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.40.00.00.00-recent30-0-0-1-1">魔幻小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.44.00.00.00-recent30-0-0-1-1">情感小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.31.00.00.00-recent30-0-0-1-1">中国近现代小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.52.00.00.00-recent30-0-0-1-1">影视小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.42.00.00.00-recent30-0-0-1-1">武侠小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.39.00.00.00-recent30-0-0-1-1">惊悚/恐怖小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.47.00.00.00-recent30-0-0-1-1">乡土小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.43.00.00.00-recent30-0-0-1-1">军事小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.46.00.00.00-recent30-0-0-1-1">都市小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.49.00.00.00-recent30-0-0-1-1">财经小说</a></li>
                        <li class=""><a href="http://bang.dangdang.com/books/bestsellers/01.03.48.00.00.00-recent30-0-0-1-1">职场小说</a></li>
                    </ul>
                <div class="side_nav" category_path="01.05.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.05.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">文学</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.21.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.21.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">成功/励志</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.36.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.36.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">历史</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.09.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.09.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">动漫/幽默</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.28.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.28.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">哲学/宗教</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.45.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.45.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">外语</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.31.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.31.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">心理学</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.01.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.01.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">青春文学</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.22.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.22.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">管理</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.07.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.07.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">艺术</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.18.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.18.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">保健/养生</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.15.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.15.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">亲子/家教</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.27.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.27.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">政治/军事</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.52.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.52.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">科普读物</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.30.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.30.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">社会科学</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.38.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.38.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">传记</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.32.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.32.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">古籍</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.49.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.49.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">教材</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.26.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.26.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">法律</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.25.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.25.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">经济</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.24.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.24.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">投资理财</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.54.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.54.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">计算机/网络</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.34.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.34.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">文化</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.56.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.56.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">医学</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.12.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.12.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">旅游/地图</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.47.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.47.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">考试</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.17.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.17.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">育儿/早教</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.63.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.63.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">工业技术</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.06.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.06.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">孕产/胎教</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.20.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.20.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">手工/DIY</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.10.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.10.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">烹饪/美食</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.19.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.19.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">体育/运动</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.04.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.04.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">休闲/爱好</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.50.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.50.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">工具书</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.62.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.62.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">自然科学</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.55.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.55.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">建筑</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.16.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.16.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">两性关系</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.14.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.14.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">家庭/家居</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.11.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.11.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">时尚/美妆</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
                <div class="side_nav" category_path="01.66.00.00.00.00">
            <a href="http://bang.dangdang.com/books/bestsellers/01.66.00.00.00.00-recent30-0-0-1-1" onclick="javascript:window.event.stopPropagation();">农业/林业</a><span class="icon"></span>
        </div>
        <ul class="side_nav_detail">
                    </ul>
            </div>
    <div class="bang_nav">
    <div class="side_title">当当图书榜</div>
        <div class="side_nav"><a href="http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1">图书畅销榜</a></div> 
        <div class="side_nav"><a href="http://bang.dangdang.com/books/newhotsales/01.00.00.00.00.00-24hours-0-0-1-1">新书热卖榜</a></div> 
        <div class="side_nav"><a href="http://bang.dangdang.com/books/childrensbooks/01.41.00.00.00.00-24hours-0-0-1-1">童书榜</a></div> 
        <div class="side_nav"><a href="http://bang.dangdang.com/books/hotbang">热搜榜</a></div> 
        <div class="side_nav"><a href="http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1">好评榜</a></div> 
        <div class="side_nav"><a href="http://bang.dangdang.com/books/soaringsales/01.00.00.00.00.00-0-0-0-1-1">飙升榜</a></div> 
        <div class="side_nav"><a href="http://bang.dangdang.com/books/surplusbooks/01.00.00.00.00.00-recent7-0-0-1-1">特价榜</a></div> 
        <div class="side_nav"><a href="http://e.dangdang.com/rank_detail_page.html?listType=ddds_sale&amp;channelType=all&amp;timeDimension=2">电子书畅销榜</a></div> 
        <div class="side_nav"><a href="http://e.dangdang.com/rank_detail_page.html?listType=ddds_new&amp;channelType=all&amp;payType=1&amp;timeDimension=2">电子书新书热卖榜</a></div> 
        </div>
    <div class="bang_nav" style="display: none">
    <div class="side_title">推荐排行</div>  
    <div class="side_nav"><a href="http://bang.dangdang.com/music/bestSeller/">音乐畅销榜</a></div>
    <div class="side_nav"><a href="http://bang.dangdang.com/movie/bestSeller/">影视畅销榜</a></div>
    <div class="side_nav"><a href="http://bang.dangdang.com/mall/bestSeller/">百货畅销榜</a></div>
    </div>
    <!--left ads-->
    <!-- 广告 modify-->
<!--<div name="__AD-L" align=center style="margin-top:12px;margin-bottom:12px;width:178px; height:240px; border:1px solid #d3d3d3; overflow:hidden;"> <a target="_blank" href=""> <img src="" width="180" /></a> </div>-->
<!-- 广告 end-->

<!-- 左侧分类广告位 add chaichunyan 101103 begin -->
<ul class="bang_list_ads">
    <li>
<div id="ad_cpt_11144" class=""></div><script>DD_ADSMART.fetchCPT(11144)</script>
    </li>
    <li>
<div id="ad_cpt_11145" class=""></div><script>DD_ADSMART.fetchCPT(11145)</script>
    </li>
    <li>
<div id="ad_cpt_11146" class=""></div><script>DD_ADSMART.fetchCPT(11146)</script>
    </li>
</ul>
<!-- 左侧分类广告位 add chaichunyan 101103 end -->

      
</div>
<script type="text/javascript">
    $(document).ready(function(){
        var navs =$('#sortRanking').find('.side_nav');
        var params = {"ranking_list":"bestsellers","cat_path":"01.03.00.00.00.00","page":1,"page_size":20,"type":"recent30","year":0,"month":0,"range":0,"style":1,"debug":""};
        navs.click(function(){
            var aNav = $(this)
            var cat3 = aNav.next();
            if($.trim(cat3.html()) == ''){
                params.cat_path_clicked = aNav.attr("category_path");
                $.ajax({
                    url: "/books/category",
                    type: "post",
                    contentType: "application/json",
                    data: JSON.stringify(params),
                    success: function(html){
                        cat3.html(html);
                        cat3.slideToggle();
                        aNav.toggleClass("hover");
                    }
                });
            }else{
                cat3.slideToggle();
                aNav.toggleClass("hover");
            }

        });

        var cat_path2_prefix = "01.03.00.00.00.00".substr(0,5);

        navs.each(function(){
            var aNav = $(this);
            if(aNav.attr("category_path").substr(0,5) == cat_path2_prefix){
                aNav.trigger('click');
                return false;
            }
        });
    });
</script>
            <!--bang_list_box-->            
            <div class="bang_list_box">
                <script type="text/javascript">
$(function(){
    
//$(".mode_btn").on('click', '.mode_btn_left', function(){
$(".mode_btn span .mode_btn_left").live('click',  function(e){
    var style = $(this).attr('style_css');
//    var style = 2;
    var url = window.location.href;
    var hypen_pos = url.lastIndexOf('-');
//    alert(hypen_pos);
    if(hypen_pos>0){
        var new_url_head = url.substring(0, parseInt(hypen_pos)-1);
//        alert(new_url_head);
        var new_url_tail = url.substring(hypen_pos);
//        alert(new_url_tail);
        var new_url = new_url_head+style+new_url_tail;
//        alert(new_url);   
    }else{
        var new_url = url.replace(/(\/$)/g,"")+'/'+style+'-1';
//        alert(new_url);         
    }
    window.location.href = new_url;
    e.preventDefault();
});

$(".mode_btn span .mode_btn_right").live('click', function(e){
    var style = $(this).attr('style_css');
//    alert(style);
//    var style = 2;
    var url = window.location.href;
    var hypen_pos = url.lastIndexOf('-');
//    alert(hypen_pos);
    if(hypen_pos>0){
        var new_url_head = url.substring(0, parseInt(hypen_pos)-1);
//        alert(new_url_head);
        var new_url_tail = url.substring(hypen_pos);
//        alert(new_url_tail);
        var new_url = new_url_head+style+new_url_tail;
//        alert(new_url);   
    }else{
        var new_url = url.replace(/(\/$)/g,"")+'/'+style+'-1';
//        alert(new_url);         
    }
    window.location.href = new_url; 
    e.preventDefault();
});

})    
</script>

<div class="bang_list_date">
    
<p><span class="left">近&nbsp;日</span>
   <span class="date_list">
                
        <a href="http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-24hours-0-0-1-1">近24小时</a>
        <a href="http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-recent7-0-0-1-1">近7日</a>
        <a href="http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-recent30-0-0-1-1" class="now">近30日</a>

            </span>
</p>



 
<p class="last"><span class="left">往&nbsp;年</span>
   <span class="date_list">
                                                <a href="http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-year-2022-0-1-1">2022年</a>       
                                <a href="http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-year-2023-0-1-1">2023年</a>       
                                <a href="http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-year-2024-0-1-1">2024年</a>       
                                <a href="http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-year-2025-0-1-1">2025年</a>
               
    </span>
</p>    
            
        
</div>
                <div class="fanye_top">
<div class="data"><a class="arrow_l"></a><span class="or">1</span><span>/25</span><a class="arrow_r arrow_r_on" href="javascript:loadData('2');"></a></div><script type="text/javascript">function __g(p){if(isNaN(p) || parseInt(p)!=p || p<=0 || p>25)alert('页码必须是1-25的整数');else javascript:loadData(document.getElementById('t__cp').value);};function bindEvent(obj){obj.onkeypress=function(e){if((arguments[0] || window.event).keyCode==13)  __g(this.value);}};function loadData(page){window.location.href="/books/bestsellers/01.03.00.00.00.00-recent30-0-0-1-"+parseInt(page)}</script><div class="mode_btn">
<span class="mode_pic"><a href="javascript:;" style_css="1" class="mode_btn_left" title="大图"></a><a href="javascript:;" style_css="2" class="mode_btn_right" title="列表"></a></span>    
</div>
</div>
<ul class="bang_list clearfix bang_list_mode">
    
    
   
    <li class="">
    <div class="list_num red">1.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29311943.html" target="_blank"><img src="http://img3m3.ddimg.cn/23/25/29311943-1_l_1747301862.jpg" alt="活着（余华代表作，精装，易烊千玺推荐阅读）" title="活着（余华代表作，精装，易烊千玺推荐阅读）"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29311943.html" target="_blank" title="活着（余华代表作，精装，易烊千玺推荐阅读）">活着（余华代表作，精装，易烊千玺推荐阅读）</a></div>    
    <div class="star"><span class="level"><span style="width: 90.4%;"></span></span><a href="http://product.dangdang.com/29311943.html?point=comment_point" target="_blank">1765115条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=余华" title="余华  著 ，新经典  出品" target="_blank">余华</a>  著 ，<a href="http://search.dangdang.com/?key=新经典" title="余华  著 ，新经典  出品" target="_blank">新经典</a>  出品</div>    
    <div class="publisher_info"><span>2021-10-01</span>&nbsp;<a href="http://search.dangdang.com/?key=北京十月文艺出版社" target="_blank">北京十月文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥31.00</span>
                        <span class="price_r">¥45.00</span>
            (<span class="price_s">6.9折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29311943');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29311943" name="" href="javascript:showMsgBox('addto_favorlist_29311943',encodeURIComponent('29311943&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li class="">
    <div class="list_num red">2.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29437347.html" target="_blank"><img src="http://img3m7.ddimg.cn/93/36/29437347-1_l_1753777168.jpg" alt="一句顶一万句 刘震云作品 印签版 茅盾文学奖 专享印签本当当自营孟非" title="一句顶一万句 刘震云作品 印签版 茅盾文学奖 专享印签本当当自营孟非"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29437347.html" target="_blank" title="一句顶一万句 刘震云作品 印签版 茅盾文学奖 专享印签本当当自营孟非">一句顶一万句 刘震云作品 印签版 茅盾文学奖 专享印签本当当自营<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 97.2%;"></span></span><a href="http://product.dangdang.com/29437347.html?point=comment_point" target="_blank">804912条评论</a><span class="tuijian">99.9%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=刘震云" title="刘震云，长江新世纪 出品" target="_blank">刘震云</a>，<a href="http://search.dangdang.com/?key=长江新世纪" title="刘震云，长江新世纪 出品" target="_blank">长江新世纪</a> 出品</div>    
    <div class="publisher_info"><span>2022-08-01</span>&nbsp;<a href="http://search.dangdang.com/?key=广东花城出版社" target="_blank">广东花城出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥34.00</span>
                        <span class="price_r">¥68.00</span>
            (<span class="price_s">5.0折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29437347');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29437347" name="" href="javascript:showMsgBox('addto_favorlist_29437347',encodeURIComponent('29437347&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li class="">
    <div class="list_num red">3.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29667984.html" target="_blank"><img src="http://img3m4.ddimg.cn/60/15/29667984-1_l_1723168851.jpg" alt="十日终焉1囚笼" title="十日终焉1囚笼"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29667984.html" target="_blank" title="十日终焉1囚笼">十日终焉1囚笼</a></div>    
    <div class="star"><span class="level"><span style="width: 92.8%;"></span></span><a href="http://product.dangdang.com/29667984.html?point=comment_point" target="_blank">82806条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=杀虫队队员" title="杀虫队队员，风炫文化 出品" target="_blank">杀虫队队员</a>，<a href="http://search.dangdang.com/?key=风炫文化" title="杀虫队队员，风炫文化 出品" target="_blank">风炫文化</a> 出品</div>    
    <div class="publisher_info"><span>2023-12-01</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥29.80</span>
                        <span class="price_r">¥46.80</span>
            (<span class="price_s">6.4折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29667984');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29667984" name="" href="javascript:showMsgBox('addto_favorlist_29667984',encodeURIComponent('29667984&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li class="">
    <div class="list_num ">4.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29728513.html" target="_blank"><img src="http://img3m3.ddimg.cn/1/12/29728513-1_l_1716187545.jpg" alt="十日终焉2迷城" title="十日终焉2迷城"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29728513.html" target="_blank" title="十日终焉2迷城">十日终焉2迷城</a></div>    
    <div class="star"><span class="level"><span style="width: 97.8%;"></span></span><a href="http://product.dangdang.com/29728513.html?point=comment_point" target="_blank">72232条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=杀虫队队员" title="杀虫队队员，风炫文化 出品" target="_blank">杀虫队队员</a>，<a href="http://search.dangdang.com/?key=风炫文化" title="杀虫队队员，风炫文化 出品" target="_blank">风炫文化</a> 出品</div>    
    <div class="publisher_info"><span>2024-04-01</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥29.80</span>
                        <span class="price_r">¥46.80</span>
            (<span class="price_s">6.4折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29728513');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29728513" name="" href="javascript:showMsgBox('addto_favorlist_29728513',encodeURIComponent('29728513&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li class="">
    <div class="list_num ">5.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29858553.html" target="_blank"><img src="http://img3m3.ddimg.cn/54/34/29858553-1_l_1745806024.jpg" alt="十日终焉6白羊" title="十日终焉6白羊"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29858553.html" target="_blank" title="十日终焉6白羊">十日终焉6白羊</a></div>    
    <div class="star"><span class="level"><span style="width: 84.2%;"></span></span><a href="http://product.dangdang.com/29858553.html?point=comment_point" target="_blank">41621条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=杀虫队队员" title="杀虫队队员，风炫文化 出品" target="_blank">杀虫队队员</a>，<a href="http://search.dangdang.com/?key=风炫文化" title="杀虫队队员，风炫文化 出品" target="_blank">风炫文化</a> 出品</div>    
    <div class="publisher_info"><span>2025-03-22</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥31.50</span>
                        <span class="price_r">¥48.00</span>
            (<span class="price_s">6.6折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29858553');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29858553" name="" href="javascript:showMsgBox('addto_favorlist_29858553',encodeURIComponent('29858553&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li class="">
    <div class="list_num ">6.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29823549.html" target="_blank"><img src="http://img3m9.ddimg.cn/96/32/29823549-1_l_1739415295.jpg" alt="十日终焉5万相" title="十日终焉5万相"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29823549.html" target="_blank" title="十日终焉5万相">十日终焉5万相</a></div>    
    <div class="star"><span class="level"><span style="width: 91%;"></span></span><a href="http://product.dangdang.com/29823549.html?point=comment_point" target="_blank">51142条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=杀虫队队员" title="杀虫队队员，风炫文化 出品" target="_blank">杀虫队队员</a>，<a href="http://search.dangdang.com/?key=风炫文化" title="杀虫队队员，风炫文化 出品" target="_blank">风炫文化</a> 出品</div>    
    <div class="publisher_info"><span>2025-01-01</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥31.50</span>
                        <span class="price_r">¥46.80</span>
            (<span class="price_s">6.7折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29823549');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29823549" name="" href="javascript:showMsgBox('addto_favorlist_29823549',encodeURIComponent('29823549&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li class="">
    <div class="list_num ">7.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29786039.html" target="_blank"><img src="http://img3m9.ddimg.cn/8/3/29786039-1_l_1730444159.jpg" alt="十日终焉4乐园" title="十日终焉4乐园"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29786039.html" target="_blank" title="十日终焉4乐园">十日终焉4乐园</a></div>    
    <div class="star"><span class="level"><span style="width: 94.6%;"></span></span><a href="http://product.dangdang.com/29786039.html?point=comment_point" target="_blank">64115条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=杀虫队队员" title="杀虫队队员，风炫文化 出品" target="_blank">杀虫队队员</a>，<a href="http://search.dangdang.com/?key=风炫文化" title="杀虫队队员，风炫文化 出品" target="_blank">风炫文化</a> 出品</div>    
    <div class="publisher_info"><span>2024-09-30</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥31.50</span>
                        <span class="price_r">¥48.00</span>
            (<span class="price_s">6.6折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29786039');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29786039" name="" href="javascript:showMsgBox('addto_favorlist_29786039',encodeURIComponent('29786039&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li class="">
    <div class="list_num ">8.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29741943.html" target="_blank"><img src="http://img3m3.ddimg.cn/66/11/29741943-1_l_1722231491.jpg" alt="十日终焉3不息" title="十日终焉3不息"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29741943.html" target="_blank" title="十日终焉3不息">十日终焉3不息</a></div>    
    <div class="star"><span class="level"><span style="width: 98.2%;"></span></span><a href="http://product.dangdang.com/29741943.html?point=comment_point" target="_blank">69431条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=杀虫队队员" title="杀虫队队员，风炫文化 出品" target="_blank">杀虫队队员</a>，<a href="http://search.dangdang.com/?key=风炫文化" title="杀虫队队员，风炫文化 出品" target="_blank">风炫文化</a> 出品</div>    
    <div class="publisher_info"><span>2024-06-01</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥31.50</span>
                        <span class="price_r">¥48.00</span>
            (<span class="price_s">6.6折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29741943');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29741943" name="" href="javascript:showMsgBox('addto_favorlist_29741943',encodeURIComponent('29741943&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li class="">
    <div class="list_num ">9.</div>   
    <div class="pic"><a href="http://product.dangdang.com/26186058.html" target="_blank"><img src="http://img3m8.ddimg.cn/63/11/26186058-1_l_1751427994.jpg" alt="悉达多 人民日报推荐 心动的信号7彭高翁青雅同款，翻译家姜乙译本【果麦经典】" title="悉达多 人民日报推荐 心动的信号7彭高翁青雅同款，翻译家姜乙译本【果麦经典】"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/26186058.html" target="_blank" title="悉达多 人民日报推荐 心动的信号7彭高翁青雅同款，翻译家姜乙译本【果麦经典】">悉达多 人民日报推荐 心动的信号7彭高翁青雅同款，翻译家姜乙译本<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 91.6%;"></span></span><a href="http://product.dangdang.com/26186058.html?point=comment_point" target="_blank">749516条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info">[德]<a href="http://search.dangdang.com/?key=赫尔曼·黑塞" title="[德]赫尔曼·黑塞，译者：姜乙，果麦文化 出品" target="_blank">赫尔曼·黑塞</a>，译者：<a href="http://search.dangdang.com/?key=姜乙" title="[德]赫尔曼·黑塞，译者：姜乙，果麦文化 出品" target="_blank">姜乙</a>，<a href="http://search.dangdang.com/?key=果麦文化" title="[德]赫尔曼·黑塞，译者：姜乙，果麦文化 出品" target="_blank">果麦文化</a> 出品</div>    
    <div class="publisher_info"><span>2017-01-01</span>&nbsp;<a href="http://search.dangdang.com/?key=天津人民出版社" target="_blank">天津人民出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥16.00</span>
                        <span class="price_r">¥32.00</span>
            (<span class="price_s">5.0折</span>)
                    </p>
                    <p class="price_e">电子书：<span class="price_n">¥32.00</span></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('26186058');" class="listbtn_buy">加入购物车</a>
                        
                        <a name="" href="http://product.dangdang.com/1900668045.html" class="listbtn_buydz" target="_blank">购买电子书</a>
              
            <a ddname="加入收藏" id="addto_favorlist_26186058" name="" href="javascript:showMsgBox('addto_favorlist_26186058',encodeURIComponent('26186058&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">10.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29930838.html" target="_blank"><img src="http://img3m8.ddimg.cn/69/21/29930838-1_l_1761718944.jpg" alt="十日终焉7极道  当当自营 杀虫队队员无限流" title="十日终焉7极道  当当自营 杀虫队队员无限流"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29930838.html" target="_blank" title="十日终焉7极道  当当自营 杀虫队队员无限流">十日终焉7极道  当当自营 杀虫队队员无限流</a></div>    
    <div class="star"><span class="level"><span style="width: 90.2%;"></span></span><a href="http://product.dangdang.com/29930838.html?point=comment_point" target="_blank">18196条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=杀虫队队员" title="杀虫队队员，风炫文化 出品" target="_blank">杀虫队队员</a>，<a href="http://search.dangdang.com/?key=风炫文化" title="杀虫队队员，风炫文化 出品" target="_blank">风炫文化</a> 出品</div>    
    <div class="publisher_info"><span>2025-09-01</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥38.50</span>
                        <span class="price_r">¥48.00</span>
            (<span class="price_s">8.0折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29930838');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29930838" name="" href="javascript:showMsgBox('addto_favorlist_29930838',encodeURIComponent('29930838&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li class="">
    <div class="list_num ">11.</div>   
    <div class="pic"><a href="http://product.dangdang.com/27878108.html" target="_blank"><img src="http://img3m8.ddimg.cn/5/14/27878108-1_l_1723007328.jpg" alt="额尔古纳河右岸（茅盾文学奖获奖作品全集28）" title="额尔古纳河右岸（茅盾文学奖获奖作品全集28）"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/27878108.html" target="_blank" title="额尔古纳河右岸（茅盾文学奖获奖作品全集28）">额尔古纳河右岸（茅盾文学奖获奖作品全集28）</a></div>    
    <div class="star"><span class="level"><span style="width: 96.8%;"></span></span><a href="http://product.dangdang.com/27878108.html?point=comment_point" target="_blank">1214561条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=迟子建" title="迟子建" target="_blank">迟子建</a></div>    
    <div class="publisher_info"><span>2019-06-01</span>&nbsp;<a href="http://search.dangdang.com/?key=人民文学出版社" target="_blank">人民文学出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥17.60</span>
                        <span class="price_r">¥32.00</span>
            (<span class="price_s">5.5折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('27878108');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_27878108" name="" href="javascript:showMsgBox('addto_favorlist_27878108',encodeURIComponent('27878108&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">12.</div>   
    <div class="pic"><a href="http://product.dangdang.com/23579654.html" target="_blank"><img src="http://img3m4.ddimg.cn/32/35/23579654-1_l_1740123779.jpg" alt="三体全3册套装三体123黑暗森林死神永生： 刘慈欣代表作，亚洲“雨果奖”获奖作品！中国科幻基石丛书 科幻小说代表作" title="三体全3册套装三体123黑暗森林死神永生： 刘慈欣代表作，亚洲“雨果奖”获奖作品！中国科幻基石丛书 科幻小说代表作"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/23579654.html" target="_blank" title="三体全3册套装三体123黑暗森林死神永生： 刘慈欣代表作，亚洲“雨果奖”获奖作品！中国科幻基石丛书 科幻小说代表作">三体全3册套装三体123黑暗森林死神永生： 刘慈欣代表作，亚洲“雨<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 96.8%;"></span></span><a href="http://product.dangdang.com/23579654.html?point=comment_point" target="_blank">2591231条评论</a><span class="tuijian">99.9%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=刘慈欣" title="刘慈欣" target="_blank">刘慈欣</a></div>    
    <div class="publisher_info"><span>2010-11-01</span>&nbsp;<a href="http://search.dangdang.com/?key=重庆出版社" target="_blank">重庆出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥55.80</span>
                        <span class="price_r">¥93.00</span>
            (<span class="price_s">6.0折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('23579654');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_23579654" name="" href="javascript:showMsgBox('addto_favorlist_23579654',encodeURIComponent('23579654&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">13.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29771967.html" target="_blank"><img src="http://img3m7.ddimg.cn/93/28/29771967-1_l_1749636776.jpg" alt="红岩 八年级上册阅读名著正版原著罗广斌杨益言著爱国主义红色经典书籍初中生课外书中国青年出版社" title="红岩 八年级上册阅读名著正版原著罗广斌杨益言著爱国主义红色经典书籍初中生课外书中国青年出版社"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29771967.html" target="_blank" title="红岩 八年级上册阅读名著正版原著罗广斌杨益言著爱国主义红色经典书籍初中生课外书中国青年出版社">红岩 八年级上册阅读名著正版原著罗广斌杨益言著爱国主义红色经典<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 87.4%;"></span></span><a href="http://product.dangdang.com/29771967.html?point=comment_point" target="_blank">290640条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=罗广斌" title="罗广斌,杨益言著" target="_blank">罗广斌</a>,<a href="http://search.dangdang.com/?key=杨益言" title="罗广斌,杨益言著" target="_blank">杨益言</a>著</div>    
    <div class="publisher_info"><span>2024-08-01</span>&nbsp;<a href="http://search.dangdang.com/?key=中国青年出版社" target="_blank">中国青年出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥38.40</span>
                        <span class="price_r">¥48.00</span>
            (<span class="price_s">8.0折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29771967');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29771967" name="" href="javascript:showMsgBox('addto_favorlist_29771967',encodeURIComponent('29771967&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">14.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29914884.html" target="_blank"><img src="http://img3m4.ddimg.cn/54/14/29914884-1_l_1759050742.jpg" alt="此刻是春天 卢思浩2025全新长篇力作  纵使世界寒冬  但我耕种春天 当当自营" title="此刻是春天 卢思浩2025全新长篇力作  纵使世界寒冬  但我耕种春天 当当自营"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29914884.html" target="_blank" title="此刻是春天 卢思浩2025全新长篇力作  纵使世界寒冬  但我耕种春天 当当自营">此刻是春天 卢思浩2025全新长篇力作  纵使世界寒冬  但我耕种春天<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 95.8%;"></span></span><a href="http://product.dangdang.com/29914884.html?point=comment_point" target="_blank">128949条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=卢思浩" title="卢思浩 著,博集天卷 出品" target="_blank">卢思浩</a> 著,<a href="http://search.dangdang.com/?key=博集天卷" title="卢思浩 著,博集天卷 出品" target="_blank">博集天卷</a> 出品</div>    
    <div class="publisher_info"><span>2025-07-01</span>&nbsp;<a href="http://search.dangdang.com/?key=湖南文艺出版社" target="_blank">湖南文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥33.70</span>
                        <span class="price_r">¥51.80</span>
            (<span class="price_s">6.5折</span>)
                    </p>
                    <p class="price_e">电子书：<span class="price_n">¥41.99</span></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29914884');" class="listbtn_buy">加入购物车</a>
                        
                        <a name="" href="http://product.dangdang.com/1901384147.html" class="listbtn_buydz" target="_blank">购买电子书</a>
              
            <a ddname="加入收藏" id="addto_favorlist_29914884" name="" href="javascript:showMsgBox('addto_favorlist_29914884',encodeURIComponent('29914884&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">15.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29845066.html" target="_blank"><img src="http://img3m6.ddimg.cn/31/15/29845066-1_l_1757039290.jpg" alt="窄门（典藏插图版）诺贝尔文学奖得主纪德巅峰之作！傅雷翻译奖得主李玉民的法语直译本。余华读到浑身发抖，想要写出来的小说！" title="窄门（典藏插图版）诺贝尔文学奖得主纪德巅峰之作！傅雷翻译奖得主李玉民的法语直译本。余华读到浑身发抖，想要写出来的小说！"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29845066.html" target="_blank" title="窄门（典藏插图版）诺贝尔文学奖得主纪德巅峰之作！傅雷翻译奖得主李玉民的法语直译本。余华读到浑身发抖，想要写出来的小说！">窄门（典藏插图版）诺贝尔文学奖得主纪德巅峰之作！傅雷翻译奖得<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 94.4%;"></span></span><a href="http://product.dangdang.com/29845066.html?point=comment_point" target="_blank">74071条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info">[法]<a href="http://search.dangdang.com/?key=安德烈·纪德" title="[法]安德烈·纪德 著 李玉民 译，紫图图书 出品" target="_blank">安德烈·纪德</a> 著 <a href="http://search.dangdang.com/?key=李玉民" title="[法]安德烈·纪德 著 李玉民 译，紫图图书 出品" target="_blank">李玉民</a> 译，<a href="http://search.dangdang.com/?key=紫图图书" title="[法]安德烈·纪德 著 李玉民 译，紫图图书 出品" target="_blank">紫图图书</a> 出品</div>    
    <div class="publisher_info"><span>2025-02-01</span>&nbsp;<a href="http://search.dangdang.com/?key=四川人民出版社" target="_blank">四川人民出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥22.00</span>
                        <span class="price_r">¥55.00</span>
            (<span class="price_s">4.0折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29845066');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29845066" name="" href="javascript:showMsgBox('addto_favorlist_29845066',encodeURIComponent('29845066&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">16.</div>   
    <div class="pic"><a href="http://product.dangdang.com/25479247.html" target="_blank"><img src="http://img3m7.ddimg.cn/13/11/25479247-1_l_1751428003.jpg" alt="窄门（诺贝尔文学奖经典 读完《窄门》便读懂了纪德的一生 法文直译全新版 “你希望很快忘记吗？—我希望永远不忘”）" title="窄门（诺贝尔文学奖经典 读完《窄门》便读懂了纪德的一生 法文直译全新版 “你希望很快忘记吗？—我希望永远不忘”）"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/25479247.html" target="_blank" title="窄门（诺贝尔文学奖经典 读完《窄门》便读懂了纪德的一生 法文直译全新版 “你希望很快忘记吗？—我希望永远不忘”）">窄门（诺贝尔文学奖经典 读完《窄门》便读懂了纪德的一生 法文直<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 91.8%;"></span></span><a href="http://product.dangdang.com/25479247.html?point=comment_point" target="_blank">552597条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info">[法] <a href="http://search.dangdang.com/?key=安德烈·纪德" title="[法] 安德烈·纪德，译者 顾琪静，果麦文化 出品" target="_blank">安德烈·纪德</a>，译者 <a href="http://search.dangdang.com/?key=顾琪静" title="[法] 安德烈·纪德，译者 顾琪静，果麦文化 出品" target="_blank">顾琪静</a>，<a href="http://search.dangdang.com/?key=果麦文化" title="[法] 安德烈·纪德，译者 顾琪静，果麦文化 出品" target="_blank">果麦文化</a> 出品</div>    
    <div class="publisher_info"><span>2018-10-01</span>&nbsp;<a href="http://search.dangdang.com/?key=天津人民出版社" target="_blank">天津人民出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥22.50</span>
                        <span class="price_r">¥45.00</span>
            (<span class="price_s">5.0折</span>)
                    </p>
                    <p class="price_e">电子书：<span class="price_n">¥42.00</span></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('25479247');" class="listbtn_buy">加入购物车</a>
                        
                        <a name="" href="http://product.dangdang.com/1901105972.html" class="listbtn_buydz" target="_blank">购买电子书</a>
              
            <a ddname="加入收藏" id="addto_favorlist_25479247" name="" href="javascript:showMsgBox('addto_favorlist_25479247',encodeURIComponent('25479247&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">17.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29471209.html" target="_blank"><img src="http://img3m9.ddimg.cn/97/6/29471209-1_l_1755677008.jpg" alt="杀死一只知更鸟（豆瓣9.3，关于勇气与正义的成长教科书，影响全球5000万家庭的“教养宝典”，奥巴马、贝克汉姆、奥普拉鼎力推荐）" title="杀死一只知更鸟（豆瓣9.3，关于勇气与正义的成长教科书，影响全球5000万家庭的“教养宝典”，奥巴马、贝克汉姆、奥普拉鼎力推荐）"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29471209.html" target="_blank" title="杀死一只知更鸟（豆瓣9.3，关于勇气与正义的成长教科书，影响全球5000万家庭的“教养宝典”，奥巴马、贝克汉姆、奥普拉鼎力推荐）">杀死一只知更鸟（豆瓣9.3，关于勇气与正义的成长教科书，影响全球<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 96.8%;"></span></span><a href="http://product.dangdang.com/29471209.html?point=comment_point" target="_blank">1295243条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=哈珀·李" title="哈珀·李 著 李育超 译" target="_blank">哈珀·李</a> 著 <a href="http://search.dangdang.com/?key=李育超" title="哈珀·李 著 李育超 译" target="_blank">李育超</a> 译</div>    
    <div class="publisher_info"><span>2022-11-01</span>&nbsp;<a href="http://search.dangdang.com/?key=译林出版社" target="_blank">译林出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥34.80</span>
                        <span class="price_r">¥58.00</span>
            (<span class="price_s">6.0折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29471209');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29471209" name="" href="javascript:showMsgBox('addto_favorlist_29471209',encodeURIComponent('29471209&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">18.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29755264.html" target="_blank"><img src="http://img3m4.ddimg.cn/22/12/29755264-1_l_1738807992.jpg" alt="我胆小如鼠 新版上市 余华献给被原生家庭伤害过的孩子的自传，看完从胆小怯懦变得松弛强大！读客当代文学文库" title="我胆小如鼠 新版上市 余华献给被原生家庭伤害过的孩子的自传，看完从胆小怯懦变得松弛强大！读客当代文学文库"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29755264.html" target="_blank" title="我胆小如鼠 新版上市 余华献给被原生家庭伤害过的孩子的自传，看完从胆小怯懦变得松弛强大！读客当代文学文库">我胆小如鼠 新版上市 余华献给被原生家庭伤害过的孩子的自传，看<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 92.2%;"></span></span><a href="http://product.dangdang.com/29755264.html?point=comment_point" target="_blank">152066条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=余华" title="余华;读客文化 出品" target="_blank">余华</a>;<a href="http://search.dangdang.com/?key=读客文化" title="余华;读客文化 出品" target="_blank">读客文化</a> 出品</div>    
    <div class="publisher_info"><span>2024-05-30</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥35.80</span>
                        <span class="price_r">¥49.90</span>
            (<span class="price_s">7.2折</span>)
                    </p>
                    <p class="price_e">电子书：<span class="price_n">¥49.90</span></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29755264');" class="listbtn_buy">加入购物车</a>
                        
                        <a name="" href="http://product.dangdang.com/1901361827.html" class="listbtn_buydz" target="_blank">购买电子书</a>
              
            <a ddname="加入收藏" id="addto_favorlist_29755264" name="" href="javascript:showMsgBox('addto_favorlist_29755264',encodeURIComponent('29755264&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">19.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29490306.html" target="_blank"><img src="http://img3m6.ddimg.cn/87/11/29490306-1_l_8.jpg" alt="第七天（2024年百班千人寒假书单 九年级推荐阅读）（2022版，余华长篇小说经典，比《活着》更绝望，比《兄弟》更荒诞，获华语文学传媒大奖）" title="第七天（2024年百班千人寒假书单 九年级推荐阅读）（2022版，余华长篇小说经典，比《活着》更绝望，比《兄弟》更荒诞，获华语文学传媒大奖）"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29490306.html" target="_blank" title="第七天（2024年百班千人寒假书单 九年级推荐阅读）（2022版，余华长篇小说经典，比《活着》更绝望，比《兄弟》更荒诞，获华语文学传媒大奖）">第七天（2024年百班千人寒假书单 九年级推荐阅读）（2022版，余华<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 98.8%;"></span></span><a href="http://product.dangdang.com/29490306.html?point=comment_point" target="_blank">657545条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=余华" title="余华  著， 新经典  出品" target="_blank">余华</a>  著， <a href="http://search.dangdang.com/?key=新经典" title="余华  著， 新经典  出品" target="_blank">新经典</a>  出品</div>    
    <div class="publisher_info"><span>2022-12-01</span>&nbsp;<a href="http://search.dangdang.com/?key=新星出版社" target="_blank">新星出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥36.70</span>
                        <span class="price_r">¥49.00</span>
            (<span class="price_s">7.5折</span>)
                    </p>
                    <p class="price_e">电子书：<span class="price_n">¥23.70</span></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29490306');" class="listbtn_buy">加入购物车</a>
                        
                        <a name="" href="http://product.dangdang.com/1901276819.html" class="listbtn_buydz" target="_blank">购买电子书</a>
              
            <a ddname="加入收藏" id="addto_favorlist_29490306" name="" href="javascript:showMsgBox('addto_favorlist_29490306',encodeURIComponent('29490306&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
   
    <li>
    <div class="list_num ">20.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29902792.html" target="_blank"><img src="http://img3m2.ddimg.cn/40/21/29902792-1_l_1753267499.jpg" alt="刘楚昕新书泥潭 当当自营现货专享作者印签寄语限量藏书票 漓江文学奖获奖作品 现货充足下单优先发货 当当自营" title="刘楚昕新书泥潭 当当自营现货专享作者印签寄语限量藏书票 漓江文学奖获奖作品 现货充足下单优先发货 当当自营"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29902792.html" target="_blank" title="刘楚昕新书泥潭 当当自营现货专享作者印签寄语限量藏书票 漓江文学奖获奖作品 现货充足下单优先发货 当当自营">刘楚昕新书泥潭 当当自营现货专享作者印签寄语限量藏书票 漓江文<span class="dot">...</span></a></div>    
    <div class="star"><span class="level"><span style="width: 82.8%;"></span></span><a href="http://product.dangdang.com/29902792.html?point=comment_point" target="_blank">449162条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=刘楚昕" title="刘楚昕" target="_blank">刘楚昕</a></div>    
    <div class="publisher_info"><span>2025-06-11</span>&nbsp;<a href="http://search.dangdang.com/?key=漓江出版社" target="_blank">漓江出版社</a></div>    
                          
    
    <div class="price">        
        <p>
            <span class="price_n">¥29.80</span>
                        <span class="price_r">¥42.00</span>
            (<span class="price_s">7.1折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29902792');" class="listbtn_buy">加入购物车</a>
                        
              
            <a ddname="加入收藏" id="addto_favorlist_29902792" name="" href="javascript:showMsgBox('addto_favorlist_29902792',encodeURIComponent('29902792&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
        </div>
        
    </div>
  
    </li>    
    
</ul>
<!--paginating-->
<div class="paginating"><ul class="paging" name="Fy"><li class="prev none"><a href="javascript:void(0);" class="fanye_page fanye_none">上一页</a></li><li><a href="javascript:loadData('1');" class="current">1</a></li><li><a href="javascript:loadData('2');">2</a></li><li><a href="javascript:loadData('3');">3</a></li><li><span>...</span></li><li><a href="javascript:loadData('24');">24</a></li><li><a href="javascript:loadData('25');">25</a></li><li class="next"><a href="javascript:loadData('2');">下一页</a></li><li class="page_input"><span>到第</span><input id="t__cp" type="text" class="number number_hover" value="1">
                    <span>页</span><input class="button" id="click_get_page" value="确定" type="button" onclick="javascript:__g(document.getElementById('t__cp').value)"></li></ul></div><script type="text/javascript">function __g(p){if(isNaN(p) || parseInt(p)!=p || p<=0 || p>25)alert('页码必须是1-25的整数');else javascript:loadData(document.getElementById('t__cp').value);};function bindEvent(obj){obj.onkeypress=function(e){if((arguments[0] || window.event).keyCode==13)  __g(this.value);}};function loadData(page){window.location.href="/books/bestsellers/01.03.00.00.00.00-recent30-0-0-1-"+parseInt(page)}</script>
            </div> 
        </div>
        
    </div><a id="ddchangeaccalert" tabindex="9" style="position: absolute; left: 0px; top: 0px; display: block; width: 0px; height: 0px; overflow: hidden;">新窗口打开无障碍说明页面,按Ctrl加波浪键打开导盲模式</a>
    <div class="fixedbar">
        <a href="javascript:scroll(0,0)"></a>
    </div>    
    <!--预留footer区-->
        <div id="footer">
	<link href="//static.dangdang.com/css/header2012/footer_150526.css?20170626" rel="stylesheet" type="text/css">
	<style>.footer_copyright img {display: inline;}.footer_ad_img{width:auto;height:52px;}.footer_link_img {width: auto;height: 47px;}.footer_ad_new_inner{display: flex;align-items: center;justify-content: center;gap: 50px;}.footer_ad_new_inner a {margin: 12px 0;}</style>
	<div class="footer" dd_name="页尾">
	        <!--页尾广告 -->
							<div class="footer_pic_new">
					<div class="footer_ad_new_inner">

								<a name="foot_1" href="http://help.dangdang.com/details/page13" target="_blank" class="footer_img"><img class="footer_ad_img" src="https://platform-permanent.ddimg.cn/pt-front-cms-upload-file/2025/12/18/2025121818204782872.png"></a>
								<a name="foot_2" href="http://help.dangdang.com/details/page16" target="_blank" class="footer_img"><img class="footer_ad_img" src="https://platform-permanent.ddimg.cn/pt-front-cms-upload-file/2025/12/18/2025121818204823486.png"></a>
								<a name="foot_3" href="http://help.dangdang.com/details/page28" target="_blank" class="footer_img"><img class="footer_ad_img" src="https://platform-permanent.ddimg.cn/pt-front-cms-upload-file/2025/12/18/202512181820475322.png"></a>

					</div>
				</div>
				<!--帮助中心的模版 -->
				<div class="public_footer_new" style="display: flex;justify-content: center;gap: 20px;padding: 10px 0 20px 0;width: auto;min-height: 140px;height:auto">

							<div class="footer_sort footer_nvice" style="float: none;width: auto;">
								<span class="f_title">购物指南</span>
								<ul>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page2" target="_blank" class="main" rel="nofollow">购买流程</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page6" target="_blank" rel="nofollow">发票制度</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page12" target="_blank" rel="nofollow">服务协议</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page8" target="_blank" rel="nofollow">会员优惠</a></li>
								</ul>
							</div>
							<div class="footer_sort footer_nvice" style="float: none;width: auto;">
								<span class="f_title">支付方式</span>
								<ul>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page22" target="_blank" class="main" rel="nofollow">网上支付</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page24" target="_blank" rel="nofollow">礼品卡支付</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page23" target="_blank" rel="nofollow">银行转账</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page25" target="_blank" rel="nofollow">礼券支付</a></li>
								</ul>
							</div>
							<div class="footer_sort footer_nvice" style="float: none;width: auto;">
								<span class="f_title">订单服务</span>
								<ul>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page400" target="_blank" class="main" rel="nofollow">配送服务查询</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page4" target="_blank" rel="nofollow">订单状态说明</a></li>
										<li><a name="foot_gouwu" href="http://myhome.dangdang.com/myOrder" target="_blank" rel="nofollow">自助取消订单</a></li>
										<li><a name="foot_gouwu" href="http://myhome.dangdang.com/myOrder" target="_blank" rel="nofollow">自助修改订单</a></li>
								</ul>
							</div>
							<div class="footer_sort footer_nvice" style="float: none;width: auto;">
								<span class="f_title">配送方式</span>
								<ul>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page232" target="_blank" class="main" rel="nofollow">当日递</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page233" target="_blank" rel="nofollow">次日达</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page500" target="_blank" rel="nofollow">订单自提</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page20" target="_blank" rel="nofollow">验货与签收</a></li>
								</ul>
							</div>
							<div class="footer_sort footer_nvice" style="float: none;width: auto;">
								<span class="f_title">退换货</span>
								<ul>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page28" target="_blank" class="main" rel="nofollow">退换货服务查询</a></li>
										<li><a name="foot_gouwu" href="http://return.dangdang.com/reverseapplyselect.aspx" target="_blank" rel="nofollow">自助申请退换货</a></li>
										<li><a name="foot_gouwu" href="http://return.dangdang.com/reverseapplylist.aspx" target="_blank" rel="nofollow">退换货进度查询</a></li>
										<li><a name="foot_gouwu" href="http://help.dangdang.com/details/page31" target="_blank" rel="nofollow">退款方式和时间</a></li>
								</ul>
							</div>
							<div class="footer_sort footer_nvice" style="float: none;width: auto;">
								<span class="f_title">商家服务</span>
								<ul>
										<li><a name="foot_gouwu" href="http://shop.dangdang.com/shangjia" target="_blank" class="main" rel="nofollow">商家中心</a></li>
										<li><a name="foot_gouwu" href="http://outlets.dangdang.com/merchants_cooperation" target="_blank" rel="nofollow">运营服务</a></li>
								</ul>
							</div>
				</div>

		<div class="footer_nav_box">

						<div class="footer_nav" style="padding-bottom: 0;">
								<a href="http://t.dangdang.com/companyInfo" target="_blank" rel="nofollow">公司简介</a>
								<span class="sep">|</span>
								<a href="https://union.dangdang.com/" target="_blank" rel="nofollow">网站联盟</a>
								<span class="sep">|</span>
								<a href="http://outlets.dangdang.com/merchants_open" target="_blank" rel="nofollow">当当招商</a>
								<span class="sep">|</span>
								<a href="http://b2b.dangdang.com/ddRegistered?custId=2c21d394a078586625dec5580df4f63f&amp;sid=pc_98735b14bad55caea349809381b6f78b3e4a0196fd574b70356e84727b559d46" target="_blank" rel="nofollow">机构销售</a>
								<span class="sep">|</span>
								<a href="http://t.dangdang.com/20130220_ydmr" target="_blank" rel="nofollow">手机当当</a>
								<span class="sep">|</span>
								<a href="http://blog.dangdang.com/" target="_blank" rel="nofollow">官方Blog</a>
								<span class="sep">|</span>
								<a href="http://t.dangdang.com/intellectualProperty" target="_blank" rel="nofollow"> 知识产权 </a>
								<span class="sep">|</span>
								<a href="http://www.dangdang.com/" target="_blank" rel="nofollow">热词搜索</a>
								
						</div>


				<div class="footer_copyright">
						<div class="footer_copyright" style="padding: 10px 0px 0px; margin: 0px auto; float: none; width: 960px; text-align: center; color: #8c8c8c; line-height: 20px; font-family: 'Microsoft YaHei'; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: #ffffff; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span style="display: inline-block; float: none;">Copyright 2004 - 2024 当当网. All Rights Reserved</span></div>
<div class="footer_copyright" style="padding: 10px 0px 0px; margin: 0px auto; float: none; width: 960px; text-align: center; color: #8c8c8c; line-height: 20px; font-family: 'Microsoft YaHei'; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: #ffffff; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span style="display: inline-block; float: none;">京ICP证041189号</span><span class="sep" style="display: inline-block; float: none; margin: 0px 17px 0px 19px;">|</span><a style="color: #8c8c8c; text-decoration: none; font-size: 12px; padding: 0px 4px;" href="https://img63.ddimg.cn/2022/6/20/2022062015355773458.jpg" target="_blank" rel="noopener"><span style="display: inline-block; float: none;">出版物经营许可证 新出发京批字第直0673号</span></a><span class="sep" style="display: inline-block; float: none; margin: 0px 17px 0px 19px;">|</span><a style="color: #8c8c8c; text-decoration: none; font-size: 12px; padding: 0px 4px;" href="https://img62.ddimg.cn/upload_img/00790/myoder/2spzgz-1620734062.jpg" target="_blank" rel="noopener"><span style="display: inline-block; float: none;">食品经营许可证：JY11101050363440</span></a><br><a style="color: #8c8c8c; text-decoration: none; font-size: 12px; padding: 0px 4px;" href="http://beian.miit.gov.cn/" target="_blank" rel="noopener"><span style="display: inline-block; float: none;">京ICP备17043473号-1</span></a><span class="sep" style="display: inline-block; float: none; margin: 0px 17px 0px 19px;">|</span><a style="color: #8c8c8c; text-decoration: none; font-size: 12px; padding: 0px 4px;" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502037644" target="_blank" rel="noopener"><img style="margin: 0px; padding: 0px; list-style-type: none; border: 0px; font-size: 12px; vertical-align: middle;" src="https://img60.ddimg.cn/assets/pc_image/jinggongwanganbei.png" alt="京公网安备 11010502037644号"><span style="display: inline-block; float: none; margin-left: 5px;">京公网安备11010502037644号</span></a><span class="sep" style="display: inline-block; float: none; margin: 0px 17px 0px 19px;">|</span><a style="color: #8c8c8c; text-decoration: none; font-size: 12px; padding: 0px 4px;" href="https://img63.ddimg.cn/upload_img/00790/wuxian/TJICP-1638451281.jpg" target="_blank" rel="noopener"><span style="display: inline-block; float: none;">经营许可证编号：合字B2-20160011</span></a><span class="sep" style="display: inline-block; float: none; margin: 0px 17px 0px 19px;">|</span><a style="color: #8c8c8c; text-decoration: none; font-size: 12px; padding: 0px 4px;" href="https://img63.ddimg.cn/upload_img/00753/123/123-1589788783.jpg" target="_blank" rel="noopener"><span style="display: inline-block; float: none;">互联网药品信息服务资格证</span></a><br><span style="display: inline-block; float: none;">互联网违法和不良信息举报电话：4001066666-5，涉未成年举报电话：4001066666-9，邮箱：<a style="color: #8c8c8c; text-decoration: none; font-size: 12px; padding: 0px 4px;" href="mailto:jubao@dangdang.com">jubao@dangdang.com</a></span><br><span style="display: inline-block; float: none;"><a style="color: #8c8c8c; text-decoration: none; font-size: 12px; padding: 0px 4px;" href="https://img62.ddimg.cn/upload_img/00753/123/2-1592548881.jpg" target="_blank" rel="noopener">北京当当科文电子商务有限公司</a>，通信地址：北京市东城区藏经馆胡同17号1幢A103室</span></div>
				</div>


				<div class="footer_icon footer_icon2" style="padding-left:20px;width: 100%;display: flex;align-items: center;justify-content: center;gap: 20px;padding-top: 20px;box-sizing: border-box;">

							<div class="logo3">
									<a href="http://www.dangdang.com/" target="_blank">
										<img class="footer_link_img" src="http://img61.ddimg.cn/7d593c48-48f6-4fc9-85e0-7d6e10dfc2a2.hpvgUvc9" alt="友情链接">
									</a>
							</div>
							<div class="logo4">
									<a href="https://www.pinganzhengxin.com/" target="_blank">
										<img class="footer_link_img" src="http://img63.ddimg.cn/upload_img/00111/home/brand_128_47.png" alt="友情链接">
									</a>
							</div>
							<div class="logo5">
									<a href="https://www.12377.cn/" target="_blank">
										<img class="footer_link_img" src="http://img60.ddimg.cn/upload_img/00459/home/hlwjbzx_182.png" alt="友情链接">
									</a>
							</div>
							<div class="logo6">
									<a href="http://adadm.dangdang.com/login.php" target="_blank">
										<img class="footer_link_img" src="http://img60.ddimg.cn/upload_img/00459/home/cnnic.png" alt="友情链接">
									</a>
							</div>
							<div class="logo7">
									<a href="http://www.dangdang.com/" target="_blank">
										<img class="footer_link_img" src="http://img61.ddimg.cn/ddimg/1462/acc2_icon_06-1642647403.jpg" alt="友情链接">
									</a>
							</div>

					<div class="clear"></div>
				</div>


		</div>

	</div>
</div>

<div id="footer_end"></div>
<!--CreateDate  2026-01-05 15:00:01-->    <div class="foot_tip_ad">广告</div>
    <style>
        .foot_tip_ad { width:40px; height:40px; font:12px/40px "simsun"; text-align:center; color:#fff; background-color:#474747; position:fixed; right:0; bottom:10px;_position:absolute; _bottom:auto;_top:expression(eval(document.documentElement.scrollTop+document.documentElement.clientHeight-this.offsetHeight-(parseInt(this.currentStyle.marginTop,10)||0)-(parseInt(this.currentStyle.marginBottom,10)||0)));}
    </style>
<script src="//static.dangdang.com/js/login/check_snbrowse.js?20260105" type="text/javascript"></script>
<script type="text/javascript">login_session.browsePageOperate();</script>
<script type="text/javascript" src="//click.dangdang.com/js_tracker.js?20260105"></script>
<script type="text/javascript" src="//databack.dangdang.com/collect.js?20260105"></script>
<script type="text/javascript" src="//databack.dangdang.com/store.js?20260105"></script><iframe src="https://databack.dangdang.com/proxy.html?202615" width="1px" height="1px" style="border: none; display: none;"></iframe>

<!-- 页尾 begin --><!--  --><!-- 页尾 end -->
<script type="text/javascript">
$(document).ready(function(){  
$(".bang_list li").mouseover(function(){$(this).addClass("hover");})  
.mouseout(function(){$(this).removeClass("hover");});

});  
</script>    
    
        

</body><div id="immersive-translate-popup" style="all: initial"></div></html>
'''

# li结构

html1 = '''

<li class="">
    <div class="list_num red">1.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29984831.html" target="_blank"><img src="http://img3m1.ddimg.cn/8/31/29984831-1_l_1766041580.jpg" alt="修好这颗心（女性成长、个人成长、修身养性、修养身心）" title="修好这颗心（女性成长、个人成长、修身养性、修养身心）"></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29984831.html" target="_blank" title="修好这颗心（女性成长、个人成长、修身养性、修养身心）">修好这颗心（女性成长、个人成长、修身养性、修养身心）</a></div>    
    <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29984831.html?point=comment_point" target="_blank">1020条评论</a><span class="tuijian">99.9%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=粉逍遥" title="粉逍遥" target="_blank">粉逍遥</a></div>    
    <div class="publisher_info"><span>2025-12-01</span>&nbsp;<a href="http://search.dangdang.com/?key=中国经济出版社" target="_blank">中国经济出版社</a></div>    

            <div class="biaosheng">五星评分：<span>1019次</span></div>
                      
    
    <div class="price">        
        <p><span class="price_n">¥36.80</span>
                        <span class="price_r">¥59.80</span>(<span class="price_s">6.2折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29984831');" class="listbtn_buy">加入购物车</a>
                        
                        <a ddname="加入收藏" id="addto_favorlist_29984831" name="" href="javascript:showMsgBox('addto_favorlist_29984831',encodeURIComponent('29984831&amp;platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
     
        </div>

    </div>
  
    </li>

'''


with open("html.txt",'r',encoding='utf-8') as f:
    html3 = f.read()

def solve(items):
    for item in items:
        yield {
            'range':item[0],
            'imgurl':item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price':item[6]
        }


def write_info(html):
    # 排名   图片链接 name  推荐  author times
    partten0 = r'<li.*?<div class="list_num .*?">(\d+).</div>.*?<img src="(.*?)".*?<div class="name"><a.*?>(.*?)</a>.*?class="tuijian">(.*?)</span>.*?target="_blank">(.*?)</a>.*?class="biaosheng">五星评分：<span>(.*?)</span>.*?class="price_r">&yen;(.*?)</span>'

    try:

        partten = re.compile(partten0,re.S)

        items = re.findall(partten,html)

        book_items = solve(items)

        for book_item in book_items:
            print("start wirte =========> " + str(book_item))
            with open("anser.txt",'a',encoding='utf-8') as f:
                f.write(json.dumps(book_item,ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"re错误{e}")

write_info(html3)

#
# def parse_result(html):
#    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
#    items = re.findall(pattern,html)
#    for item in items:
#        yield {
#            'range': item[0],
#            'iamge': item[1],
#            'title': item[2],
#            'recommend': item[3],
#            'author': item[4],
#            'times': item[5],
#            'price': item[6]
#        }
#
# def write_item_to_file(item):
#    print('开始写入数据 ====> ' + str(item))
#    with open('book.txt', 'a', encoding='UTF-8') as f:
#        f.write(json.dumps(item, ensure_ascii=False) + '\n')
#        f.close()
# def request_dandan(url):
#    try:
#        response = requests.get(url)
#        if response.status_code == 200:
#            return response.text
#    except requests.RequestException:
#        return None
#
#
# def main(page):
#     url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
#     html = request_dandan(url)
#     items = parse_result(html)  # 解析过滤我们想要的信息
#
#     for item in items:
#         write_item_to_file(item)
#
#
# if __name__ == "__main__":
#    for i in range(1,26):
#        main(i)















# type nul > test.txt
#
# name = "2026_note.txt"
#
# if os.path.exists( name) and os.path.isfile( name):
#     # os.remove( name)
#     pass
# else:
#     os.system("type nul > " + name)
#
#
#
# # 持续记录
# while 1:
#     con = input("请输入(输入n退出)：")
#     if con == "n":break
#     with open(name, "a+", encoding="utf-8") as f:
#         dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         # print(dt)
#         f.write(dt + " " + con + "\n")



















