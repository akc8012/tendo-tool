use std::env;
mod make_file;

fn main() {
	let arguments: Vec<String> = env::args().collect();
	println!("{:?}", arguments);

	make_file::make("out/yeet.txt", "yeet to the max!");
}
