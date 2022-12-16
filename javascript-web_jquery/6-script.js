const $headerEl = $('header');
const $updateHeaderEl = $('div#update_header');

$updateHeaderEl.on('click', () => {
    $headerEl.text('New Header!!!');
});