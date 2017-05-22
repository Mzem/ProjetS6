$(function(){

    var NEXT_URL   = "/fenetre_role_choix_colonne/";

    var fileUploadSuccess = function(data){};

    var fileUploadFail = function(data){};

    var dragHandler = function(evt){
        evt.preventDefault();
    };

    var dropHandler = function(evt){
        evt.preventDefault();
        var files = evt.originalEvent.dataTransfer.files;

        var formData = new FormData();
        formData.append("file2upload", files[0]);

        var req = {
            url: "/FileWithDragDrop/",
            method: "POST",
            processData: false,
            contentType: false,
            data: formData,
            success : function(data) {
                var file = files[0].name;
                window.location = NEXT_URL + file;
            }       
        };

        var promise = $.ajax(req);
    };

    var dropHandlerSet = {
        dragover: dragHandler,
        drop: dropHandler
    };

    $(".dropbox").on(dropHandlerSet);
    //fileUploadSuccess(false); // called to ensure that we have initial data
});