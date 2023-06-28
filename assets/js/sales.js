$(function () {
    let table_orders_list = $('#table_orders_list').DataTable( {
        "processing" : true,
        "lengthMenu" : [[10,25,50,100,-1], [10,25,50,100,"All"]],
        "pageLength": 25,
        "autoWidth": false,
        "ajax": {
                 "processing": true,
                 "url": "/sales/api/orderlist?format=datatables",
             },

        "deferRender": false,
        columns: [
                {data: "order_id"},
                {data: "date_added"},
                {data: "company", defaultContent: "" },
                {data: "firstname" ,
                    render: function (data, type, row, meta) {
                    return data + ' ' + row['lastname']
                    }
                },
                {
                data: "date_shipped",
                className: 'text-end',
                render: function ( data, type, row ) {
                    let shipping_image = ''


                    let shipping_colour = 'btn-grey'
                    if(data != null){
                        shipping_colour = 'btn-green disabled'
                    }

                        let btn_grp = '<div class="btn-group" role="group" aria-label="Shipping status">'
                        if(row['shipped_by_company']){
                            shipping_image = '<img class="img-responsive" role="button" height="25px" src="/static/images/admin/' + row['shipped_by_company'] + '_logo.png">'
                        }
                        else {
                             shipping_image = '<img role="button" class="img-responsive" height="25px" src="/static/images/admin/notshipped_logo.png">'
                        }
                        let shipping_icon = '<button id="js-shipping-dlg" type="button" class="btn btn-sm '+ shipping_colour + '" data-url="'+row['order_id']+'/shipping" data-dlgsize="model-lg"><i class="fas fa-shipping-fast "></i></button>'

                    return btn_grp + shipping_image + shipping_icon + '</div>'
                }
            },
            {data: 'shipped_by_company', "visible": false}
            ]
    } );



    $(document).on("click", "#js-shipping-dlg", loadForm);
});


var loadForm = function () {
    var btn = $(this);  // <-- HERE
    let dlg_size = btn.attr("data-dlgsize");
    let tmp_url = btn.attr("data-url");
    $("#modal-base .modal-content").html("<html><body></body></html>");
    $.ajax({
        url: btn.attr("data-url"),  // <-- AND HERE
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
            $("#modal-base #modal-outer").removeClass('modal-sm model-lg modal-xl')
            $("#modal-base #modal-outer").addClass(dlg_size)
            $("#modal-base").modal("show");
        },

        success: function (data) {
            if (data.form_is_valid) {
                $("#modal-base").modal("hide")
            } else {
                // $("#modal-base .modal-title").html("Edit Address");
                $("#modal-base .modal-content").html(data.html_form);
            }
        },
    })
};