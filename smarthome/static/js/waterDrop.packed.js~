/*************************************************************
 * This script is developed by Arturs Sosins aka ar2rsawseen, http://webcodingeasy.com
 * Feel free to distribute and modify code, but keep reference to its creator
 *
 * Water drop provides a drip effect on HTML objects as standalone 
 * package and jquery plugin. It is possible to configure, speed, 
 * color, field and toggle animations as fading and expanding.
 *
 * For more information, examples and online documentation visit: 
 * http://webcodingeasy.com/JS-classes/Water-drop-effect
**************************************************************/
(function( $ ){
	$.fn.waterDrop = function() {
		//some configuration
		var conf = {
			//event where to attach effect
			event: "click",
			//width of border
			borderWidth: 2,
			//style of border
			borderStyle: "solid",
			//color of border
			borderColor: "black",
			//border radius
			borderRadius: 5,
			//background color
			backgroundColor: "white",
			//padding from original element
			padding: 0,
			//fadeOut effect
			fadeOut: true,
			//expand effect
			expand: true,
			//animation speed
			speed: 10,
			//animation progress
			step: 1,
			//total animation steps
			expandSteps: 50,
			//reverse effect
			reverse: false,
			//callback function when effect ended
			onend: null
		};
		//copy settings
		if (arguments[0] && typeof arguments[0] === 'object') { 
			$.extend(conf, arguments[0]);
		}
		var action = false;
		if((arguments[0] && arguments[0] == "drop") || (arguments[1] && arguments[1] == "drop"))
		{
			action = true;
		}
		//fix types
		conf.borderRadius = parseInt(conf.borderRadius);
		conf.borderWidth = parseInt(conf.borderWidth);
		conf.padding = parseInt(conf.padding);
		var scroll = new Object();
		scroll.top = $(window).scrollTop();
		scroll.left = $(window).scrollLeft();
		$(window).bind("resize", function() {
			scroll.top = $(window).scrollTop();
			scroll.left = $(window).scrollLeft();
		});
		//apply to each element
		return this.each(function() {   
			var $this = $(this);
			var dropAction = function(){
				var off = $this.offset();
				if(conf.reverse)
				{
					var rev = (conf.step*conf.expandSteps);
					drop.style.top = ((off.top-conf.padding)-rev) + "px";
					drop.style.left = ((off.left-conf.padding)-rev) + "px";
					drop.style.width = ($this.outerWidth() + conf.padding*2 + rev*2) + "px";
					drop.style.height = ($this.outerHeight() + conf.padding*2 + rev*2) + "px";
					drop.style.display = "block";
					$(drop).css("opacity", 0);
				}
				else
				{
					drop.style.top = (off.top-conf.padding) + "px";
					drop.style.left = (off.left-conf.padding) + "px";
					drop.style.width = ($this.outerWidth() + conf.padding*2) + "px";
					drop.style.height = ($this.outerHeight() + conf.padding*2) + "px";
					drop.style.display = "block";
					$(drop).css("opacity", 1);
				}
				var animObject = new Object();
				if(conf.expand)
				{
					animObject.top = (conf.reverse) ? "+=" + (conf.step*conf.expandSteps) : "-=" + (conf.step*conf.expandSteps);
					animObject.left = (conf.reverse) ? "+="+ (conf.step*conf.expandSteps) : "-="+ (conf.step*conf.expandSteps);
					animObject.width = (conf.reverse) ? "-="+ ((conf.step*conf.expandSteps)*2) : "+="+ ((conf.step*conf.expandSteps)*2);
					animObject.height = (conf.reverse) ? "-="+ ((conf.step*conf.expandSteps)*2) : "+="+ ((conf.step*conf.expandSteps)*2);
				}
				if(conf.fadeOut)
				{
					animObject.opacity = (conf.reverse) ? 1 : 0;
				}
				$(drop).animate(animObject, conf.expandSteps*conf.speed, function() {
					$(drop).css("display", "none");
					if(conf.onend)
					{
						conf.onend();
					}
				});
			};
			var drop = document.createElement("div");
			drop.style.position = "absolute";
			drop.style.display = "none";
			drop.style.borderWidth = conf.borderWidth + "px";
			drop.style.borderStyle = conf.borderStyle;
			drop.style.borderColor = conf.borderColor;
			drop.style.borderRadius = conf.borderRadius + "px";
			drop.style.MozBorderRadius = conf.borderRadius + "px";
			drop.style.WebkitBorderRadius = conf.borderRadius + "px";
			drop.style.backgroundColor = conf.backgroundColor;
			drop.style.zIndex = 9999;
			document.body.appendChild(drop);
			if(conf.event.length > 0)
			{
				$this.bind(conf.event, function(event){
					event.stopPropagation();
					dropAction()
				});
			}
			if(action)
			{
				dropAction();
			}
		});
	};
})( jQuery );
