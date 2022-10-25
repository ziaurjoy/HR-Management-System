


// DELETE FUNCTION SWEETALERT
function SweetDelete(e,href){
  e.preventDefault()
  var self = $(this)
  Swal.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete it!'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Deleted!',
        'Your file has been deleted.',
        'success',
      )
      location.href = href
    }
  })
}


$(document).ready(function() {
  $("#select_index").select2({
  });
});



$("#id_mother_organization").change(function () { 
  var mother_organizationId = $(this).val();  
  $.ajax({                       
  url: ajax_load_sister_organization_url,
  data: {
    'mother_organization_id': mother_organizationId   
  },
  success: function (data) { 
    $("#id_sister_organization").html(data);  
    }
  });
});



