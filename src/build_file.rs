use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

pub fn make(path: &str, text: &str) {
	let path = Path::new(path);

	let file = create_file(path);
	write_to_file(path, file, text);
}

fn create_file(path: &Path) -> File {
	match File::create(&path) {
		Err(why) => panic!("Couldn't create {}: {}", path.display(), why.description()),
		Ok(file) => file,
	}
}

fn write_to_file(path: &Path, mut file: File, text: &str) {
	match file.write_all(text.as_bytes()) {
		Err(why) => panic!(
			"Couldn't write to {}: {}",
			path.display(),
			why.description()
		),
		Ok(_) => println!("Successfully wrote to {}", path.display()),
	}
}
