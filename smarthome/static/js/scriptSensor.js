/*jslint white: true, browser: true, undef: true, nomen: true, eqeqeq: true, plusplus: false, bitwise: true, regexp: true, strict: true, newcap: true, immed: true, maxerr: 14 */
/*global window: false, REDIPS: true, $: true */

/* enable strict mode */
"use strict";

// global variables  
var redips = {},		// redips container
	rd = REDIPS.drag,	// reference to the REDIPS.drag library
	counter = 0,		// counter for cloned DIV elements
	clonedDIV = false,	// cloned flag set in event.moved
	lastCell;			// reference to the last cell in table


// redips initialization
redips.init = function () {
    // set reference to the last cell in table
    lastCell = document.getElementById('lastCell');
    // initialization
    rd.init();
    // elements can be dropped only to the empty table cells
    rd.dropMode = 'overwrite';
    // shift DIV elements with animation
    rd.shift.animation = true;
    // disabled elements will have opacity effect
    rd.style.opacityDisabled = 50;
    // set hover color
    rd.hover.colorTd = 'transparent';
    rd.hover.borderTd = '2px solid red';
    // confirm DIV element delete action
    //rd.trash.question = 'Esta seguro de eliminar el sensor?';
    // event handler invoked before DIV element is dropped to the cell

    // display target and source position of dropped element
    rd.event.dropped = function () {
        // get target and source position (method returns positions as array)
        // pos[0] - target table index
        // pos[1] - target row index
        // pos[2] - target cell (column) index
        // pos[3] - source table index
        // pos[4] - source row index
        // pos[5] - source cell (column) index
        var pos = rd.getPosition();
        if (pos[0] == '1') {
            var position = 0;

            if (pos[1] == 0) {
                position = pos[2] + 1;
            }
            else {
                position = (pos[1] * 20) + (pos[2] + 1)
            }

            /*is_discrete true: 1 /false: 0*/
            var is_discrete = 0;
            var typeSensor = rd.obj.id.substring(0, 1);

            /*Tipo de sensores*/
            //Sensor :0
            //Actuador :1
            var description = $('#descriptionSensor').val();
            if (description == '') {
                if (typeSensor == 'p') {
                    description = 'Sensor de Puertas';
                }
                else if (typeSensor == 'm') {
                    description = 'Sensor de Movimiento';
                }
                else if (typeSensor == 'h') {
                    description = 'Sensor de Humo';
                }
                else if (typeSensor == 't') {
                    description = 'Actuador de Temperatura';
                }
                else if (typeSensor == 'l') {
                    description = 'Actuador de Luz';
                }
            }

            var type = 1;
            if (typeSensor == 'p' || typeSensor == 'm' || typeSensor == 'h') {
                type = 0;
                is_discrete = 1;
            }

            // how to test TD if cell is occupied

            var sensorTB = $("#planoTabla");
            var sensorTD = sensorTB.find('td[id="' + position + '"]');
            var d = sensorTD.html();

     

            add_sensor(rd.obj.id, description, position, type, is_discrete);
            $('#descriptionSensor').val('');

            //Borramos un sensor arrastrado en la misma tabla del plano
            if (pos[3] == '1') {

                var position = 0;

                if (pos[4] == 0) {
                    position = pos[5] + 1;
                }
                else {
                    position = (pos[4] * 20) + (pos[5] + 1)
                }

                delete_sensor(position);
                $('#tableDataSensor tbody #tr' + position).remove();
                //rd.deleteObject(rd.obj);
            }
        }
    };

    rd.event.deleted = function () {
        var pos = rd.getPosition();
        var position = 0;

        if (pos[4] == 0) {
            position = pos[5] + 1;
        }
        else {
            position = (pos[4] * 20) + (pos[5] + 1)
        }
        delete_sensor(position);
        $('#tableDataSensor tbody #tr' + position).remove();
    };

    rd.event.droppedBefore = function (targetCell) {
        // get target and source position (method returns positions as array)
        // pos[0] - target table index
        // pos[1] - target row index
        // pos[2] - target cell (column) index
        // pos[3] - source table index
        // pos[4] - source row index
        // pos[5] - source cell (column) index
        var empty = rd.emptyCell(targetCell, 'test');

        if (!empty) {
            return false;
        }
    };

    // add counter to cloned element name
    // (after cloned DIV element is dropped to the table)
    rd.event.cloned = function () {
        // increase counter
        counter++;
    };
    // in the moment when DIV element is moved, clonedDIV will be set
    rd.event.moved = function (cloned) {
        clonedDIV = cloned;
    };

};



// add onload event listener
if (window.addEventListener) {
    window.addEventListener('load', redips.init, false);
}
else if (window.attachEvent) {
    window.attachEvent('onload', redips.init);
}

function get_property_info_by_name() {
    if ($("#select_as_owner").val() == '0') {
        alert('Seleccione una propiedad');
        return;
    }
    document.getElementById("get_property_info_by_name").submit();
}

function set_sensor(positionSensor, code, sensorId) {
    try {
        var styleCode = '';
        var typeSensor = code.substring(0, 1);
        if (typeSensor == 'p') {
            styleCode = 'p';
        }
        else if (typeSensor == 'm') {
            styleCode = 'm';
        }
        else if (typeSensor == 'h') {
            styleCode = 'h';
        }
        else if (typeSensor == 't') {
            styleCode = 't';
        }
        else if (typeSensor == 'l') {
            styleCode = 'l';
        }

        var sensorTB = $("#planoTabla");
        var sensorTD = sensorTB.find('td[id="' + positionSensor + '"]')
        sensorTD.html('<div style="border-style: solid; cursor: move;" id="' + styleCode + '-' + sensorId + '" class="drag ' + styleCode + '">' + styleCode.toUpperCase() + '</div>');


    }
    catch (ex) {
        alert(ex.message);
    }
}

function add_sensor(code, description, location_in_plan, type, is_discrete) {

    var dataSensor = {
        property: $("#select_as_owner").val(),
        code: code,
        description: description,
        type: type,
        location_in_plan: location_in_plan,
        is_discrete: is_discrete
    };

    $.ajax({
        url: "/watchapp/set_position_ajax/", // the endpoint
        type: "POST", // http method
        data: JSON.stringify(dataSensor), // data sent with the delete request
        contentType: "application/json;charset=utf-8",
        async: 'true',
        success: function (data) {
            //alert(data.code);
            //set_sensor(data.location_in_plan,  data.code, data.sensor_id);

            var type = 'Actuador';
            if (data.type == 0) {
                type = 'Sensor';
            }

            var dataHTML = '    <tr id="tr' + data.location_in_plan + '">' +
                    '<td onmouseover="onSensor(' + data.location_in_plan + ',"");" onmouseleave="leaveSensor(' + data.location_in_plan + ',"");">' + data.code + '</td>' +
                    '<td onmouseover="onSensor(' + data.location_in_plan + ',"");" onmouseleave="leaveSensor(' + data.location_in_plan + ',"");">' + data.description + '</td>' +
                    '<td onmouseover="onSensor(' + data.location_in_plan + ',"");" onmouseleave="leaveSensor(' + data.location_in_plan + ',"");">' +
            type

            + '</td>' +
                    '<td onmouseover="onSensor(' + data.location_in_plan + ',"");" onmouseleave="leaveSensor(' + data.location_in_plan + ',"");">' + data.location_in_plan + '</td>' +
               ' </tr>';
            $('#tableDataSensor tbody').append(dataHTML);

        },
        error: function (xhr, errmsg, err) {
            //alert(errmsg);// provide a bit more info about the error to the console
        }
    });
}

function delete_sensor(location_in_plan) {

    var dataSensor = {
        property: $("#select_as_owner").val(),
        location_in_plan: location_in_plan
    };

    $.ajax({
        url: "/watchapp/delete_position_ajax/", // the endpoint
        type: "DELETE", // http method
        data: JSON.stringify(dataSensor), // data sent with the delete request
        contentType: "application/json;charset=utf-8",
        async: 'true',
        success: function (data) {

        },
        error: function (xhr, errmsg, err) {
            //alert(errmsg);// provide a bit more info about the error to the console
        }
    });
}


function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

function setRow(control) {
    for (var i = 1 ; i <= 400; i++) {
        $('#tr' + i).css('background', 'transparent');
    }
    $("#tr" + control.id).css('background', '#109bce');
}
