jQuery(document).ready(function () {


  // loader
  setTimeout(function () {
    $('.loaders').fadeOut();
  }, 200);




  //mobile menu
  $(".closes").click(function () {
    $(".menu-area").removeClass("mobile");

    return false;
  });


  $(".mob").click(function (event) {
    $(".menu-area").addClass("mobile");
    event.stopPropagation();
  });

  $('.contents').click(function (event) {
    if (!$(event.target).hasClass('menu-area')) {
      $(".menu-area").removeClass("mobile");
    }
  });

  $('.header-area').click(function (event) {
    if (!$(event.target).hasClass('search-category')) {
      $(".menu-area").removeClass("mobile");
    }
  });



  $('.menu > ul > li > a').click(function () {
    $('.menu > ul > li > a').removeClass("active");
    $(this).addClass("active");
  });

  $('.sub-menu > li > a').click(function () {
    $('.sub-menu > li > a').removeClass("subActive");
    $(this).addClass("subActive");

  });




  $(".menuwidth").click(function () {
    $(".menu-area").toggleClass("menu-full");
    $(".hide-item").toggleClass("show-item");
    $(".small-logo").toggleClass("show-logo");
    $(".main-contents").toggleClass("menu-full-body");

  });

  //submenu
  $('nav > ul > li > a').on('click', function (e) {
    e.stopPropagation();
    $('nav ul ul').slideUp();
    $(this).next().is(":visible") || $(this).next().slideDown();
  });

  $('.sub-menu > li > a').on('click', function (e) {
    e.stopPropagation();
    $('.sub-menu ul').slideUp();
    $(this).next().is(":visible") || $(this).next().slideDown();
  });



  $(".select2").select2({
    tags: true
  });



});

