$(document).ready(function() {
    $("#ddlCountry,#ddlAge").on("change", function() {
        var country = $('#ddlCountry').find("option:selected").val();
        var age = $('#ddlAge').find("option:selected").val();
        SearchData(country, age)
    });
});

function SearchData(country, age) {
    if (country.toUpperCase() == 'ALL' && age.toUpperCase() == 'ALL') {
        $('#myTable tbody tr').show();
    } else {
        $('#myTable tbody tr:has(td)').each(function() {
            var rowCountry = $.trim($(this).find('td:eq(9)').text());
            var rowAge = $.trim($(this).find('td:eq(10)').text());
            if (country.toUpperCase() != 'ALL' && age.toUpperCase() != 'ALL') {
                if (rowCountry.toUpperCase() == country.toUpperCase() && rowAge == age) {
                    $(this).show();
                } else {
                    $(this).hide();
                }
            } else if ($(this).find('td:eq(9)').text() != '' || $(this).find('td:eq(9)').text() != '') {
                if (country != 'all') {
                    if (rowCountry.toUpperCase() == country.toUpperCase()) {
                        $(this).show();
                    } else {
                        $(this).hide();
                    }
                }
                if (age != 'all') {
                    if (rowAge == age) {
                        $(this).show();
                    } else {
                        $(this).hide();
                    }
                }
            }

        });
    }
}