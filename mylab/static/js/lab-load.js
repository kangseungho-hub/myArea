window.addEventListener("DOMContentLoaded", (e) => {
    addDocumentSelectReLoad()
    loadDocumentList()

      selectDirectory.addEventListener("change", (e) =>{
        addDocumentSelectReLoad()
        loadDocumentList()

        
    })
})





function addDocumentSelectReLoad(){
    var selectDirectoryIndex = selectDirectory.options["selectedIndex"]
    var selectedDirectory = selectDirectory[selectDirectoryIndex]

    documentTo.value = selectedDirectory.value
}

documentDetailButton.addEventListener

function loadDocumentList(){
    $(".document-list").load("/mylab/document_list/" + documentTo.value, function(){
        $(".load-document-detail").click((e)=>{
            $(".document-root-container").load(e.currentTarget.id)
          })
    }) 


}






