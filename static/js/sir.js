// =====================================. query selector =================================

header = document.querySelector("#heading");
start = document.querySelector("#start");
pie = document.querySelector("#pie");
result = document.querySelector("#result");


//=================================== Variables ==========================================

var map, heatmap,mvc , mcvR;
var numDeltas = 10;
var delay = 10; //milliseconds
var i =0;
var data;
var count1 = 0 ,count2 = 0;
var heatmap;

//   ============================= Color Changing Function =====================
function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}


function setColor()
{
	header.style.color = getRandomColor();
	result.style.color = getRandomColor();
  

}


setInterval(setColor,500);


// ===============================Map Event Listerner=============================================

start.addEventListener('click',initMap);


// ====================== Map Fuction ============================================================

function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: {lat: 18.775, lng: -90.434},
          mapTypeId: 'satellite'
        });


		mvc = new google.maps.MVCArray();

           // ================== Infection heatmap =============================
        heatmap = new google.maps.visualization.HeatmapLayer({
                    data: mvc,
                     map: map,
                     radius : 10

                    });


        move();

          

       }


   function move()
        {

                  // for(var k = i;k< i+50 && k < points.length;k++)
                  // {
                  //       var cur = new google.maps.LatLng(points[k]['lat'],points[k]['lng'])     
                    
                  //        mvc.push(cur);

                  //  }


                  {% for k in range(i,i+50) %}

                  	{% if k < len(SIR) %}

                  		 var cur = new google.maps.LatLng({{SIR[k].lat}},{{SIR[k].lng}})   
                  		 mvc.push(cur);

                  	{% endif %}

                  {% endfor %}
                         
                         i = k;
                         if (i < {{len(SIR)}})
                         {
		    	                        
                            count1 = i;
                            setTimeout(move,0); 
                         
                         }
       }


  // =================================================== Map Function End ==================================

  // ============================================== Pie Chart Function ================================


	pie.addEventListener('click',function()
		{
				google.charts.setOnLoadCallback(drawChart);	
		});
 
      google.charts.load('current', {'packages':['corechart']});

       function drawChart() {



      var data = google.visualization.arrayToDataTable([
          ['No of people', 'Hours per Day'],        
          ['Saved', count2],
          ['Infected',     count1],

          ['Total',points.length]
          
        ]);

        var options = {
          title: 'Infection Activity'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));


        chart.draw(data, options);
        data.setValue(0, 1,count1);
        data.setValue(1, 1,count2);
        setInterval(drawChart,5000)
      }


// ==================================== Color changing of  recovery map =========================================


function changeGradient() {
        var gradient = [
          'rgba(0, 0, 0, 0)',
          'rgba(0, 255, 255, 1)',
          'rgba(0, 191, 255, 1)',
          'rgba(0, 127, 255, 1)',
          'rgba(0, 63, 255, 1)',
          'rgba(0, 0, 255, 1)',
          'rgba(0, 0, 223, 1)',
          'rgba(0, 0, 191, 1)',
          'rgba(0, 0, 159, 1)',
          'rgba(0, 0, 127, 1)',
          'rgba(63, 0, 91, 1)',
          'rgba(127, 0, 63, 1)',
          'rgba(191, 0, 31, 1)',
          'rgba(0, 0, 0, 1)'
        ]
       
          heatmap.set('gradient', heatmap1.get('gradient') ? null : gradient);

      }







