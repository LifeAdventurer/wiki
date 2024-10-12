# Permission Tree

A tree structure that manages permissions and allows moving subtrees. This project implements a simple permission tree where each node can be public or private. When a public subtree is moved to a private node, the entire subtree becomes private.

## Features

- Create and manage a tree structure.
- Add nodes with customizable permissions (public/private).
- Move subtrees while maintaining permission rules.
- Inherit permissions from parent nodes.

## Getting Started

### Prerequisites

Ensure you have [Rust](https://www.rust-lang.org/) installed on your machine. You can install it using `rustup`:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Installation

To use the `permission-tree` library in your project, add it as a dependency in your `Cargo.toml` file:

```toml
[dependencies]
permission_tree = { git = "https://github.com/LifeAdventurer/permission-tree.git" }
```

### Usage

Here's a quick example of how to use the `permission_tree` in your code:

```rs
use permission_tree::{Permission, Tree};

fn main() {
    let mut tree = Tree::new();

    // Adding nodes with permission
    tree.add_node(1, Permission::Public); // root node
    tree.add_node(2, Permission::Public);
    tree.add_node(3, Permission::Private);
    tree.add_node(4, Permission::Public);
    tree.add_node(5, Permission::Public);

    // Connecting nodes
    tree.connect_nodes(1, 2);
    tree.connect_nodes(1, 3);
    tree.connect_nodes(2, 4);
    tree.connect_nodes(2, 5);

    println!("Initial tree:");
    tree.print_tree(1, 0);

    // Moving a public subtree (node 2 and its children) to a private node (node 3))
    tree.move_subtree(2, 3);

    println!("Tree after moving subtree rooted at node 2 under node 3:");
    println!("{}", tree.print_tree(1, 0));
}
```

### Running Tests

To run tests for the `permission_tree` library, use:

```sh
cargo test
```

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](./LICENSE) file for more details.
