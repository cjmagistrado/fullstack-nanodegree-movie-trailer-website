// Preload images
var imgs = [];
for (m in movies) {
    imgs.push(movies[m].image_url);
}
preload(imgs);