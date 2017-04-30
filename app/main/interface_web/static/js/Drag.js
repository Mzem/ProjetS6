$(function(){

    var NEXT_URL   = "/fenetre_choix_fichier/";

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
            url: "/FileWithDragDrop",
            method: "post",
            processData: false,
            contentType: false,
            data: formData
        };

        var promise = $.ajax(req);
        window.navigate = NEXT_URL + files[0]; 
    };

    var dropHandlerSet = {
        dragover: dragHandler,
        drop: dropHandler
    };

    $(".dropbox").on(dropHandlerSet);
    //fileUploadSuccess(false); // called to ensure that we have initial data
});