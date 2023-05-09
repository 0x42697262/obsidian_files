function readFile() {
  var input = document.getElementById("input-file");
  var quantum = document.getElementById("quantum").value;
  var file = input.files[0];
  var reader = new FileReader();
  reader.readAsText(file);
  reader.onload = function () {
    var content = reader.result;
    var data = {
      quantum: 4,
      process: {},
    };

    content = content.split("\n");
    content.shift();
    for (let i = 0; i < content.length; i++) {
      content[i] = content[i]
        .split("\t")
        .map((item) => item.replace(/\r/g, ""))
        .filter((item) => item !== "");

      data["process"][parseInt(i)] = {
        arrival_time: parseInt(content[i][1]),
        burst_time: parseInt(content[i][2]),
        priority: parseInt(content[i][3]),
      };
    }
    data["quantum"] = parseInt(quantum);

    console.log(data);

    // Send contents to Flask server
    sendData(data);
  };
}

function sendData(data) {
  fetch("/submitprocess", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      console.log("Data sent successfully.");
    })
    .catch((error) => {
      console.error("Error sending data:", error);
    });
}
