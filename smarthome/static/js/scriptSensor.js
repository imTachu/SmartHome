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
    rd.dropMode = 'single';
    // shift DIV elements with animation
    rd.shift.animation = true;
    // disabled elements will have opacity effect
    rd.style.opacityDisabled = 50;
    // set hover color
    rd.hover.colorTd = 'transparent';
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
        //Agregamos un sensor
        if (pos[0] == '2') {            
            var positionOld = (pos[4] + 1) * (pos[5] + 1)
            var position = (pos[1] + 1) * (pos[2] + 1)
            // display element positions
            //alert("drop" + position + ', Old' + positionOld + ', ID ' + rd.obj.id);
        }
        
    };

    // delete DIV element in event.dropped() event handler
    rd.event.finish = function () {
        //rd.deleteObject(rd.obj);
        //alert('finish');
    }

    rd.event.deleted = function () {
        var pos = rd.getPosition();
        var position = (pos[4] + 1) * (pos[5] + 1)
        // display element positions
        //alert("borrado " + position);
    };

    rd.event.droppedBefore = function (targetCell) {
        //alert(targetCell.id + " " + rd.obj.id);
        // test if target cell is occupied and set reference to the dragged DIV element
        var empty = rd.emptyCell(targetCell, 'test');
        // if target cell is not empty
        if (!empty) {
            //rd.deleteObject(rd.obj);
            //alert(rd.obj.innerHTML);
            // open dialog should be wrapped in setTimeout because of
            // removeChild and return false below
            // remove dragged DIV from from DOM (node still exists in memory)
            //rd.obj.parentNode.removeChild(rd.obj);

            // this will disable DIV elements in target cell (DIV element will be somehow marked)
            // rd.enableDrag(false, targetCell);
            // return false (deleted DIV will not be returned to source cell)
            return false;
        }
    };
    // add counter to cloned element name
    // (after cloned DIV element is dropped to the table)
    rd.event.cloned = function () {
        // increase counter
        counter++;
        // append to the DIV element name
        //textboxdescripcion
        //rd.obj.innerHTML = $('#textboxdescripcion').val() +" "+ counter;
        // rd.obj.innerHTML += $('#textboxdescripcion').val();
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