function drawChart(result){
    var dis = result["Distribution"];
    var data = Object.values(dis);
    var labels = Object.keys(dis);
    var lineColor = 'rgba(75, 192, 192, 1)';
    var lineFill = 'rgba(75, 192, 192, 0.2)'
    var options = {
        title: {
            display: true,
            text: "Monthly Income by Location"
        }
    }
    
    var ctx = document.getElementById("income-chart").getContext('2d');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                borderColor: lineColor,
                backgroundColor: lineFill,
                fill: true
            },
            ]
        },
        options: options
    });
}