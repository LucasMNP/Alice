// main.rs
// Copyright 2020~2021 Lu Neder
//
// This work may be distributed and/or modified under the
// conditions of the LaTeX Project Public License, either version 1.3
// of this license or (at your option) any later version.
// The latest version of this license is in
//   http://www.latex-project.org/lppl.txt
// and version 1.3 or later is part of all distributions of LaTeX
// version 2005/12/01 or later.
//
// This work has the LPPL maintenance status `maintained'.
//
// The Current Maintainer of this work is Lu Neder.
//
// This work consists of the files main.rs, README.md and the included original.txt example.

//Alice requires an original.txt file on the directory you're running it from.
//Alice will read the file and then type it (a line followed by an enter, then the next line).
//This way you can send the file contnent on a chat, for example, each line on a message.
//You can also tell Alice to wait some time between a line and the other.
//The first line will be written 10 seconds after you run Alice and tell the time between a line and the other,
//this way you have time to select the place where you want to input your text.
//"Alice" was just the 1st name I found on Google lol

use std::env;
use text_io::scan;
use std::fs;
use std::str;

fn main() {
    println!("Not ready yet. Use branch alice-python instead.");
    // Get command line input and save it as an args variable
    let args: String = env::args().collect();

    // Checks if the mode selected in command line was help and runs it or not
    if args.contains("help") {

        alice_help(); // Help mode

    } else {

        // Asks how many seconds between lines and save it as a t variable
        println!("How many seconds between lines?");
        let t: i32;
        scan!("{}", t);
        // Prints the t variable
        println!("{} seconds between lines", t);

        //
        let file = "original.txt";
        let open = fs::read_to_string(file);
        let mut divided = open.lines();
        println!("\n{:#?}", open);

        // Checks selected mode in command line and runs it
        if args.contains("loop") {alice_loop(t);} // Loop mode
        else {alice(t)}; // Regular mode

    };
}

// Help mode
fn alice_help() {
    println!("help");
}

// Loop mode
fn alice_loop(t: i32) {
    println!("loop ({} seconds between lines)", t);
}

//Regular mode
fn alice(t: i32) {
    println!("alice ({} seconds between lines)", t);
}
