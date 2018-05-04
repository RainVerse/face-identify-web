layui.use('form', function () {
    var form = layui.form;

    $('#img-input1').change(function () {
        var file = this.files[0];
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#preview-img1').attr("src", e.target.result).removeClass("layui-hide");
        };
        reader.readAsDataURL(file);
    });
    $('#img-input2').change(function () {
        var file = this.files[0];
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#preview-img2').attr("src", e.target.result).removeClass("layui-hide");
        };
        reader.readAsDataURL(file);
    });
    form.on('submit(img-upload-btn)', function () {
        var formData = new FormData(document.getElementById("img-upload-form"));
        console.log(formData);
        $.ajax({
            url: '/deepid/validate',
            type: 'POST',
            beforeSend: function () {
                layer.load();
            },
            success: function (retJson) {
                var ret = JSON.parse(retJson);
                layer.closeAll('loading');
                if (ret.status) {
                    $('#result-div').show();
                    $('#result-text').text('验证结果为：' + (ret.result ? '同一个人' : '非同一个人'));
                } else {
                    layer.msg(ret.message);
                }
            },
            error: function (retJson) {
                layer.closeAll('loading');
                layer.msg('error');
            },
            data: formData,
            cache: false,
            contentType: false,
            processData: false
        });
        return false;
    });
});
