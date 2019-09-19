var lineColor = 'rgba(75, 192, 192, 1)';
var lineFill = 'rgba(75, 192, 192, 0.2)'
var options = {
    title: {
        display: true,
        text: "Monthly Income by Area"
    }
}

function renderChart(data, labels) {
    var ctx = document.getElementById("mixchart").getContext('2d');
    var chart = new Chart(ctx, {
        type: 'line',
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

$("#monthlyIncomeBtn").click(
    function () {
        data = [24, 56, 78, 32];
        labels = ["100 ~ 200", "200 ~ 300", "300 ~ 400", "400 ~ 500"];
        renderChart(data, labels);
    }
)