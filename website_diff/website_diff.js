var diffidx = 0;

$(document).ready(function() {
   // highlight and scroll to the first diff element
   var cur;
   cur = $(".diff").eq(diffidx)
   cur.addClass("diff-selected");
   $(cur)[0].scrollIntoView({ behavior: "smooth", block: "center", inline: "nearest"});
});

$(document).on("keypress", function(e) {
   var cur;	
   var next;
   cur = $(".diff").eq(diffidx)
   cur.removeClass("diff-selected");
   if (e.which == 110){
     diffidx += 1;
     if (diffidx > $(".diff").length-1){
         diffidx = $(".diff").length-1;
     }
   } 
   if (e.which == 78) {
     diffidx -= 1;
     if (diffidx < 0){
     	diffidx = 0;
     }
   }
   next = $(".diff").eq(diffidx)
   next.addClass("diff-selected")
   $(next)[0].scrollIntoView({ behavior: "smooth", block: "center", inline: "nearest"});
});
