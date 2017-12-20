layui.use(['element', 'layer'], function () {
    var element = layui.element;
    var layer = layui.layer;
    var $ = layui.jquery;
    if (document.body.offsetWidth > 1530) {
        layer.open({
            type: 1,
            title: '',
            content: '<ul class="layui-nav layui-nav-tree" style="display: block;width: 100%">\n' +
            '    <li class="layui-nav-item">\n' +
            '    <a href="/" style="font-size: 150%" >RainLab</a>\n' +
            '  </li>\n' +
            '  <li class="layui-nav-item layui-nav-itemed">\n' +
            '    <a href="javascript:;">Tensorflow</a>\n' +
            '    <dl class="layui-nav-child">\n' +
            '      <dd><a href="/">DeepID-人脸验证</a></dd>\n' +
            '    </dl>\n' +
            '  </li>\n' +
            '</ul>',
            area: '250px',
            offset: ['100px', '20px'],
            shade: 0,
            resize: false,
            closeBtn: 0
        });
    }

});
