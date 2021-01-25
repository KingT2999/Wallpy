async function video_files(){
	const res = await eel.video_files()();
	
	for (let i = 0; i < res.length; i++) {
		let div = document.createElement('div');
		div.className = "wallpaper_video";
		div.innerHTML = `
		<video src="video/${res[i]}" controls></video>
		<h2 id="hi">${res[i]}</h2>
		<button class="setwallpaper" onclick="set_as_wallpaper(this)">set as wallpaper</button>`;
		document.getElementById('videos').append(div);
	}
}

video_files();

async function set_as_wallpaper(el) {
	await eel.set_as_wallpaper(el.parentElement.getElementsByTagName('h2')[0].innerHTML);
}

async function remove_wallpaper() {
	await eel.remove_wallpaper()
}