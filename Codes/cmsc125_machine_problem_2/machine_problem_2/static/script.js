function readFile() {
  var input = document.getElementById("input-file");
  var file = input.files[0];
  var reader = new FileReader();
  reader.readAsText(file);
  reader.onload = function () {
    var content = reader.result;
    console.log(content); // or do something else with the content
  };
}
