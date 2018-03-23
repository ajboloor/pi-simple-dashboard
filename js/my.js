$(document).ready(function(){
  function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
      if (rawFile.readyState === 4 && rawFile.status == "200") {
        callback(rawFile.responseText);
      }
    }
    rawFile.send(null);
  }
  readTextFile("data.json", function(text){
    var data = JSON.parse(text);
    //console.log(data);

    var config_SD_storage = {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [
            data.storage.SD.used,
            data.storage.SD.avail
          ],
          backgroundColor: [
            "#4D5360",
            "#949FB1",
          ]
        }],
        labels: [
          "Used (GB)",
          "Available (GB)"
        ]
      },
      options: {
        responsive: true,
        legend: {
          position: 'bottom',
        },
        title: {
          display: true,
          text: 'SD Card Storage'
        },
        animation: {
          animateScale: false,
          animateRotate: true
        }
      }
    };

    var config_HDD_storage = {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [
            data.storage.HDD.used,
            data.storage.HDD.avail
          ],
          backgroundColor: [
            "#4D5360",
            "#949FB1",
          ]
        }],
        labels: [
          "Used (GB)",
          "Available (GB)"
        ]
      },
      options: {
        responsive: true,
        legend: {
          position: 'bottom',
        },
        title: {
          display: true,
          text: 'HDD Storage'
        },
        animation: {
          animateScale: false,
          animateRotate: true
        }
      }
    };

    var config_RAM = {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [
            data.RAM.used,
            data.RAM.avail
          ],
          backgroundColor: [
            "#4D5360",
            "#949FB1",
          ]
        }],
        labels: [
          "Used (MB)",
          "Available (MB)"
        ]
      },
      options: {
        responsive: true,
        legend: {
          position: 'bottom',
        },
        title: {
          display: true,
          text: 'RAM Usage'
        },
        animation: {
          animateScale: false,
          animateRotate: true
        }
      }
    };

    var config_temp = {
      type: 'bar',
      data: {
        datasets: [{
          data: [
            data.temperature.internal,
            data.temperature.external
          ],
          backgroundColor: [
            "#4D5360",
            "#4D5360"
          ]
        }],
        labels: [
          "CPU Temp (C)",
          "External Temp (C)"
        ]
      },
      options: {
        responsive: true,
        legend: {
          display: false,
          position: 'bottom',
        },
        title: {
          display: true,
          text: 'Internal Temp'
        },
        animation: {
          animateScale: false,
          animateRotate: true
        },
        scales: {
          xAxes: [{
            stacked: true,
            gridLines: {
              display:false
            }
          }],
          yAxes: [{
            stacked: true,
            gridLines: {
              display:false
            }
          }]
        }
      }
    };

    var config_CPU = {
      type: 'bar',
      data: {
        datasets: [{
          data: [
            20,
            30,
            30,
            70
          ],
          backgroundColor: [
            "#4D5360",
            "#4D5360",
            "#4D5360",
            "#4D5360"
          ]
        }],
        labels: [
          "Core 1 (%)",
          "Core 2 (%)",
          "Core 3 (%)",
          "Core 4 (%)"
        ]
      },
      options: {
        responsive: true,
        legend: {
          display: false,
          position: 'bottom',
        },
        title: {
          display: true,
          text: 'CPU Core Usage'
        },
        animation: {
          animateScale: false,
          animateRotate: true
        },
        scales: {
          xAxes: [{
            stacked: true,
            gridLines: {
              display:false
            }
          }],
          yAxes: [{
            stacked: true,
            gridLines: {
              display:false
            }
          }]
        }

      }
    };

    var config_CPU_radar = {
      type: 'radar',
      data: {
        datasets: [{
          data: [
            30,
            30,
            30,
            70
          ],
          backgroundColor: "rgba(179,181,198,0.2)",
          borderColor: "#4D5360",
        }],
        labels: [
          "Core 1 (%)",
          "Core 2 (%)",
          "Core 3 (%)",
          "Core 4 (%)"
        ]
      },
      options: {
        responsive: true,
        legend: {
          display: false,
          position: 'bottom',
        },
        title: {
          display: true,
          text: 'CPU Core Usage'
        },
        animation: {
          animateScale: false,
          animateRotate: true
        },
        maintainAspectRatio: true,
        scale: {
          ticks: {
            beginAtZero: true,
            max: 100
          }
        }

      }
    };

    document.getElementById("device_name").innerHTML = "Name: " + data.device.name;
    document.getElementById("device_OS").innerHTML = "OS: " + data.device.OS;
    document.getElementById("device_internet").innerHTML = "Internet: " + data.device.internet;
    document.getElementById("device_uptime").innerHTML = "Uptime: " + data.device.uptime;

    var ctx = document.getElementById("chart_SD_storage").getContext("2d");
    document.myDoughnut = new Chart(ctx, config_SD_storage);
    var ctx = document.getElementById("chart_HDD_storage").getContext("2d");
    document.myDoughnut = new Chart(ctx, config_HDD_storage);
    var ctx = document.getElementById("chart_RAM").getContext("2d");
    document.myDoughnut = new Chart(ctx, config_RAM);

    var ctx = document.getElementById("chart_tempC").getContext("2d");
    document.myDoughnut = new Chart(ctx, config_temp);
    var ctx = document.getElementById("chart_CPU").getContext("2d");
    document.myDoughnut = new Chart(ctx, config_CPU);
    var ctx = document.getElementById("chart_CPU_radar").getContext("2d");
    document.myDoughnut = new Chart(ctx, config_CPU_radar);

  });
});
