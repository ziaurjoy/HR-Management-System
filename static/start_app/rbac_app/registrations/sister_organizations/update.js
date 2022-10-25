
// LOAD AJAX
$("#id_division").change(function () {
  var divisionId = $(this).val();  
  $.ajax({                       
    url: districts_url,
    data: {
      'division': divisionId       
    },
    success: function (data) { 
      $("#id_district").html(data);  
    }
  });
});

$("#id_district").change(function () {
  var districtId = $(this).val();  
  $.ajax({                       
    url: upazilas_url,                 
    data: {
      'district': districtId      
    },
    success: function (data) { 
      $("#id_upazila").html(data); 
    }
  });
});




// SELECT-2
$(document).ready(function() {
  $("#id_division").select2({
    
  });
});

$(document).ready(function() {
  $("#id_district").select2({

  });
});

$(document).ready(function() {
  $("#id_upazila").select2({
  });
});




// $("#id_mother_organization").change(function () { 
//   var mother_organizationId = $(this).val();  
//   $.ajax({                       
//   url: ajax_load_sister_organization_url,
//   data: {
//     'mother_organization_id': mother_organizationId   
//   },
//   success: function (data) { 
//     $("#id_sister_organization").html(data);  
//     }
//   });
// });
