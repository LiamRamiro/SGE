({    
doInit: function(cmp){
    var topo = cmp.find('topo');
    //Mathrandom() < 0.5 ? $A.util.addClass(cmp,'active') : $A.util.removeClass(cmp,'inactive');  

    var number = Math.random();
    if(number < 0.5){
        $A.util.addClass(cmp,'active');
        cmp.set("v.isTopo", true)
    }else{
        $A.util.addClass(cmp,'inactive');
        cmp.set("v.isTopo", false)  
    }
   
},
topoClick: function(cmp, event, helper){
    var isTopo = cmp.get("v.isTopo");
    var evt = $A.get("e.c:Puntuacion");
    evt.setParams({	
        "molePoints": isTopo ? 2 : 0
    });
    evt.fire();

})
