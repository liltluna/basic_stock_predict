(function(a){var c={series:{fillBetween:null}};function b(f){function e(j,g){var h;for(h=0;h<g.length;++h){if(g[h].id===j.fillBetween){return g[h]}}if(typeof j.fillBetween==="number"){if(j.fillBetween<0||j.fillBetween>=g.length){return null}return g[j.fillBetween]}return null}function d(x,E,h){if(E.fillBetween==null){return}var u=e(E,x.getData());if(!u){return}var z=h.pointsize,y=h.points,w=u.datapoints.pointsize,v=u.datapoints.points,t=[],A,B,o,C,D,g,G=E.lines.show,F=z>2&&h.format[2].y,H=G&&E.lines.steps,k=true,n=0,p=0,q,r;while(true){if(n>=y.length){break}q=t.length;if(y[n]==null){for(r=0;r<z;++r){t.push(y[n+r])}n+=z}else{if(p>=v.length){if(!G){for(r=0;r<z;++r){t.push(y[n+r])}}n+=z}else{if(v[p]==null){for(r=0;r<z;++r){t.push(null)}k=true;p+=w}else{A=y[n];B=y[n+1];C=v[p];D=v[p+1];g=0;if(A===C){for(r=0;r<z;++r){t.push(y[n+r])}g=D;n+=z;p+=w}else{if(A>C){if(G&&n>0&&y[n-z]!=null){o=B+(y[n-z+1]-B)*(C-A)/(y[n-z]-A);t.push(C);t.push(o);for(r=2;r<z;++r){t.push(y[n+r])}g=D}p+=w}else{if(k&&G){n+=z;continue}for(r=0;r<z;++r){t.push(y[n+r])}if(G&&p>0&&v[p-w]!=null){g=D+(v[p-w+1]-D)*(A-C)/(v[p-w]-C)}n+=z}}k=false;if(q!==t.length&&F){t[q+2]=g}}}}if(H&&q!==t.length&&q>0&&t[q]!==null&&t[q]!==t[q-z]&&t[q+1]!==t[q-z+1]){for(r=0;r<z;++r){t[q+z+r]=t[q+r]}t[q+1]=t[q-z+1]}}h.points=t}f.hooks.processDatapoints.push(d)}a.plot.plugins.push({init:b,options:c,name:"fillbetween",version:"1.0"})})(jQuery);