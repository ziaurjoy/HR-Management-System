jQuery(document).ready(function () {
  // loader
  setTimeout(function () {
    $('.loaders').fadeOut();
  }, 200);


  //mobile menu
  $(".closes").click(function () {
    $(".menu-area").removeClass("mobile");

    return false;
  });


  $(".mob").click(function (event) {
    $(".menu-area").addClass("mobile");
    event.stopPropagation();
  });

  $('.contents').click(function (event) {
    if (!$(event.target).hasClass('menu-area')) {
      $(".menu-area").removeClass("mobile");
    }
  });

  $('.header-area').click(function (event) {
    if (!$(event.target).hasClass('search-category')) {
      $(".menu-area").removeClass("mobile");
    }
  });


  $('.menu > ul > li > a').click(function () {
    $('.menu > ul > li > a').removeClass("active");
    $(this).addClass("active");
  });

  $('.sub-menu > li > a').click(function () {
    $('.sub-menu > li > a').removeClass("subActive");
    $(this).addClass("subActive");
  });


  $(".menuwidth").click(function () {
    $(".menu-area").toggleClass("menu-full");
    $(".hide-item").toggleClass("show-item");
    $(".small-logo").toggleClass("show-logo");
    $(".main-contents").toggleClass("menu-full-body");

  });

  //submenu
  $('nav > ul > li > a').on('click', function (e) {
    e.stopPropagation();
    $('nav ul ul').slideUp();
    $(this).next().is(":visible") || $(this).next().slideDown();
  });

  $('.sub-menu > li > a').on('click', function (e) {
    e.stopPropagation();
    $('.sub-menu ul').slideUp();
    $(this).next().is(":visible") || $(this).next().slideDown();
  });


  // $(".select2").select2({
  //   tags: true
  // });

});



// PRINT FUNCTION
jQuery(document).ready(function(){
  $('#table-pdf-button').click(function() {
    $('#export-table-data').print();
    return false;
  });
});



// TABLE EXPORT FOR EXCEL
function ExportToExcel(type, fn, dl) {
  var table_title_name = document.getElementById('table-title-name').innerHTML;
  var elt = document.getElementById('export-table-data');
  var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
  return dl ?
    XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }) :
    XLSX.writeFile(wb, fn || (table_title_name+'.' + (type || 'xlsx')));
}


// TABLE EXPORT FOR CSV
function downloadCSV(csv, filename) {
  var csvFile;
  var downloadLink;
  // CSV file
  csvFile = new Blob([csv], {type: "text/csv"});
  // Download link
  downloadLink = document.createElement("a");
  // File name
  downloadLink.download = filename;
  // Create a link to the file
  downloadLink.href = window.URL.createObjectURL(csvFile);
  // Hide download link
  downloadLink.style.display = "none";
  // Add the link to DOM
  document.body.appendChild(downloadLink);
  // Click download link
  downloadLink.click();
}

function exportTableToCSV() {
  var table_title_name = document.getElementById('table-title-name').innerHTML;
  var csv = [];
  var rows = document.querySelectorAll("table tr");
  for (var i = 0; i < rows.length; i++) {
    var row = [], cols = rows[i].querySelectorAll("td, th");
    for (var j = 0; j < cols.length; j++) 
      row.push(cols[j].innerText);
    csv.push(row.join(","));        
  }
  // Download CSV file
  downloadCSV(csv.join("\n"), table_title_name+'.csv');
}








// SELECT - 2
$(document).ready(function() {
  $("#id_mother_organization").select2({
    
  });
});




