$(document).ready(function() {



});

function generateGraph(moop, graphData) {
  console.log(graphData);
  var nums = [];
  var labels = [];
  var colors = [];
  Object.keys(graphData).forEach(function(key) {
    console.log(key + ' : ' + graphData[key]);
    labels.push(key);
    nums.push(graphData[key]);
    col = '#'+(Math.random()*0xFFFFFF<<0).toString(16);
    colors.push(col)
  });

  data = {
      datasets: [{
          data: nums,
          backgroundColor: colors,
        borderColor: colors
      }],

      // These labels appear in the legend and in the tooltips when hovering different arcs
      labels: labels,
  };


  var ctx = document.getElementById("myChart");
  var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: data,
    options: {
      legend: {
        display: false
      }
    }
  });
}
