(function(a){function b(k){var m={first:{x:-1,y:-1},second:{x:-1,y:-1},show:false,active:false};var l={};var g=null;function i(s){if(m.active){r(s);k.getPlaceholder().trigger("plotselecting",[f()])}}function h(s){if(s.which!=1){return}document.body.focus();if(document.onselectstart!==undefined&&l.onselectstart==null){l.onselectstart=document.onselectstart;document.onselectstart=function(){return false}}if(document.ondrag!==undefined&&l.ondrag==null){l.ondrag=document.ondrag;document.ondrag=function(){return false}}p(m.first,s);m.active=true;g=function(t){j(t)};a(document).one("mouseup",g)}function j(s){g=null;if(document.onselectstart!==undefined){document.onselectstart=l.onselectstart}if(document.ondrag!==undefined){document.ondrag=l.ondrag}m.active=false;r(s);if(n()){q()}else{k.getPlaceholder().trigger("plotunselected",[]);k.getPlaceholder().trigger("plotselecting",[null])}return false}function f(){if(!n()){return null}if(!m.show){return null}var u={},s=m.first,t=m.second;a.each(k.getAxes(),function(w,v){if(v.used){var x=v.c2p(s[v.direction]),y=v.c2p(t[v.direction]);u[w]={from:Math.min(x,y),to:Math.max(x,y)}}});return u}function q(){var s=f();k.getPlaceholder().trigger("plotselected",[s]);if(s.xaxis&&s.yaxis){k.getPlaceholder().trigger("selected",[{x1:s.xaxis.from,y1:s.yaxis.from,x2:s.xaxis.to,y2:s.yaxis.to}])}}function c(t,u,s){return u<t?t:(u>s?s:u)}function p(w,s){var t=k.getOptions();var u=k.getPlaceholder().offset();var v=k.getPlotOffset();w.x=c(0,s.pageX-u.left-v.left,k.width());w.y=c(0,s.pageY-u.top-v.top,k.height());if(t.selection.mode=="y"){w.x=w==m.first?0:k.width()}if(t.selection.mode=="x"){w.y=w==m.first?0:k.height()}}function r(s){if(s.pageX==null){return}p(m.second,s);if(n()){m.show=true;k.triggerRedrawOverlay()}else{d(true)}}function d(s){if(m.show){m.show=false;k.triggerRedrawOverlay();if(!s){k.getPlaceholder().trigger("plotunselected",[])}}}function e(y,u){var t,v,A,x,s=k.getAxes();for(var w in s){t=s[w];if(t.direction==u){x=u+t.n+"axis";if(!y[x]&&t.n==1){x=u+"axis"}if(y[x]){v=y[x].from;A=y[x].to;break}}}if(!y[x]){t=u=="x"?k.getXAxes()[0]:k.getYAxes()[0];v=y[u+"1"];A=y[u+"2"]}if(v!=null&&A!=null&&v>A){var z=v;v=A;A=z}return{from:v,to:A,axis:t}}function o(w,u){var s,v,t=k.getOptions();if(t.selection.mode=="y"){m.first.x=0;m.second.x=k.width()}else{v=e(w,"x");m.first.x=v.axis.p2c(v.from);m.second.x=v.axis.p2c(v.to)}if(t.selection.mode=="x"){m.first.y=0;m.second.y=k.height()}else{v=e(w,"y");m.first.y=v.axis.p2c(v.from);m.second.y=v.axis.p2c(v.to)}m.show=true;k.triggerRedrawOverlay();if(!u&&n()){q()}}function n(){var s=k.getOptions().selection.minSize;return Math.abs(m.second.x-m.first.x)>=s&&Math.abs(m.second.y-m.first.y)>=s}k.clearSelection=d;k.setSelection=o;k.getSelection=f;k.hooks.bindEvents.push(function(u,s){var t=u.getOptions();if(t.selection.mode!=null){s.mousemove(i);s.mousedown(h)}});k.hooks.drawOverlay.push(function(z,t){if(m.show&&n()){var A=z.getPlotOffset();var v=z.getOptions();t.save();t.translate(A.left,A.top);var s=a.color.parse(v.selection.color);t.strokeStyle=s.scale("a",0.8).toString();t.lineWidth=1;t.lineJoin=v.selection.shape;t.fillStyle=s.scale("a",0.4).toString();var C=Math.min(m.first.x,m.second.x)+0.5,D=Math.min(m.first.y,m.second.y)+0.5,B=Math.abs(m.second.x-m.first.x)-1,u=Math.abs(m.second.y-m.first.y)-1;t.fillRect(C,D,B,u);t.strokeRect(C,D,B,u);t.restore()}});k.hooks.shutdown.push(function(t,s){s.unbind("mousemove",i);s.unbind("mousedown",h);if(g){a(document).unbind("mouseup",g)}})}a.plot.plugins.push({init:b,options:{selection:{mode:null,color:"#e8cfac",shape:"round",minSize:5}},name:"selection",version:"1.1"})})(jQuery);