var searchbar = true;
function search_display(){
    if (searchbar){
        console.log('empty')
        document.getElementById("search").innerHTML = '<select onchange= "location = this.value;"><option selected value="">-- Select a method to search --</option><option value="javascript:decide(0)">Search by Book Name</option><option value="javascript:decide(1)">Search by Author name</option><option value="javascript:decide(2)">Search by Location</option></select>'
        searchbar = false
    }
    else{
        console.log("non empty")
        document.getElementById("search").innerHTML = ''
        searchbar = true
    }
}

function decide(n){
    var m = ["Book Name", "Author's Name", "Location"]
    document.getElementById("search_box").innerHTML = '<form class="search-container"><input type="text" id="search-bar" placeholder="Enter '+m[n]+'" onkeyup="search('+n+')" /></form>'
}

function search(n){
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("search-bar");
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("label");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[n];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}