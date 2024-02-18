({
    myAction : function(component, event, helper) {

    },
    clearlist : function(component, event, helper) {
        component.set('v.lista', []);
    },
    addToList : function(component, event, helper) {
        var lista = component.get('v.lista');
        var item = event.getParam('nombre');
        lista.push(item);
        component.set('v.lista', lista);
    }
})
