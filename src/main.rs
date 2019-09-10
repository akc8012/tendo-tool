use std::fs;
mod build_file;

fn main() {
	let filename = String::from("in/template.md");
	println!("In file {}", filename);

	let template = fs::read_to_string(filename).expect("Something went wrong reading the file");
	println!("{}", template);

	build_file::make("out/post.md", &template);
}
