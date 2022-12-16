const $listALL = $('ul.my_list');
const $addALL = $('div#add_item');

$addALL.on('click', () => {
    $listALL.append('<li>Item</li>');
});