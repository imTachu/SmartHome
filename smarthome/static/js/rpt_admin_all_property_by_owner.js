//Función para crear el reporte en formato pdf
function get_report() {
    //Oculta el div de información
    $("#divRpt").css('display', 'none');
    //Captura la fecha inicial del reporte
    var startDate = Date.parse($("#dateInit").val());
    //Captura la fecha final del reporte
    var endDate = Date.parse($("#dateFinal").val());

    //Valida las fechas
    if (startDate > endDate) {
        //Muestra el div de alertas
        $("#divAlert").css('display', 'block');
        return;
    }

    //Oculta el div de alertas
    $("#divAlert").css('display', 'none');

    //Captura los fitros del reporte en formato json
    var dataFilter = {
		owners_select: $("#owners_select").val(),
        dateInit: $("#dateInit").val() + ' 00:00:00-05',
        dateFinal: $("#dateFinal").val() + ' 23:59:59-05',
    };

    //Consume el método que genera el reporte
    $.ajax({
        url: "/watchapp/get_report_admin_all_property_by_owner/", // Endpoint
        type: "POST", // Método http
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(dataFilter),//Datos
        async: 'true',
        success: function (data) {
            if (data === '0') {
                //Si no se encuentran registros se muestra el div de información
                $("#divRpt").css('display', 'block');
            }
            else {
                //Oculta el div de información
                $("#divRpt").css('display', 'none');
                //Muestra el reporte en pdf en otra página
                window.open("data:application/pdf," + escape(data));
            }
        },
        error: function (xhr, errmsg, err) {
                $("#divRpt").css('display', 'block');
		$('#tableEvents tbody').html("");
        }
    });
}

//Función para crear el reporte en formato pdf
function get_report_data() {
    //Oculta el div de información
    $("#divRpt").css('display', 'none');
    //Captura la fecha inicial del reporte
    var startDate = Date.parse($("#dateInit").val());
    //Captura la fecha final del reporte
    var endDate = Date.parse($("#dateFinal").val());

    //Valida las fechas
    if (startDate > endDate) {
        //Muestra el div de alertas
        $("#divAlert").css('display', 'block');
        return;
    }

    //Oculta el div de alertas
    $("#divAlert").css('display', 'none');

    //Captura los fitros del reporte en formato json
    var dataFilter = {
		owners_select: $("#owners_select").val(),
        dateInit: $("#dateInit").val() + ' 00:00:00-05',
        dateFinal: $("#dateFinal").val() + ' 23:59:59-05',
    };
	$("#loading_popup").show();
    //Consume el método que genera el reporte
    $.ajax({
        url: "/watchapp/get_event_admin_all_property_by_owner/", // Endpoint
        type: "POST", // Método http
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(dataFilter),//Datos
        async: 'true',
        success: function (data) {
		$("#loading_popup").hide();
		console.log(data)
            if (data === '0') {
                //Si no se encuentran registros se muestra el div de información
                $("#divRpt").css('display', 'block');
		$('#tableEvents tbody').html("");
            }
            else {
                //Oculta el div de información
                $("#divRpt").css('display', 'none');
		$('#tableEvents tbody').html("");
				console.log(data.length)
                for (var i = 0; i < data.length; i++) {
					console.log(data[i].date)
                    var e = "<tr>" +
                    "<td>" + data[i].date + "</td>" +
                    "<td>" + data[i].type + "</td>" +
                    "<td>" + data[i].description + "</td>" +
                    "<td>" + data[i].is_critical + "</td>" +
                    "<td>" + data[i].is_fatal + "</td>" +
                    "<td>" + data[i].property + "</td>" +
                    "<td>" + data[i].sensor + "</td>" +
                    "<td>" + data[i].propietario + "</td>" +
                    "</tr>";
                    $('#tableEvents tbody').append(e);
                }
            }
        },
        error: function (xhr, errmsg, err) {
                $("#divRpt").css('display', 'block');
		$('#tableEvents tbody').html("");
        }
    });
}
