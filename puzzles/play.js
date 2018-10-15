class Foo {
	sayHi (name) {
		console.log("Hi " + name);
	}
}

class Baz extends Foo {

	sayHi(name) {
		super.sayHi(name + ' from baz');

	}
}

function Person (name) {
  if (name) { 
    this.options.name = name;
  }
};

Person.prototype.options = {
  name: 'Default name'
};

var foo = new Person('foo');
var bar = new Person('bar');

console.log(foo.options.name);
console.log(bar.options.name);


console.log(foo.options)