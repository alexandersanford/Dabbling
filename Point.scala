import scala.::
import scala.Console._
import scala.collection.immutable.Nil.:::
import scala.util.Random

case class Point(x: Int, y: Int)

trait Iterator[A] {
  def hasNext: Boolean
  def next: A
}

//class IntIterator(to: Int) extends Iterator[Int] {
//  private var current = 0
//  override def hasNext: Boolean = current < to
//  override def next: Int = {
//    if (hasNext)
//
//  }
//}



object Point {
  def main(args: Array[String]): Unit = {
    val list: List[Any] = List(
      "a string",
      732,
      'c',
      true,
      () => "an anonymous function returning a string"
    )
    list.foreach(element => println(element))


    val point = Point(1, 2)
    //val anotherPoint = Point(1, 2)
    val yetAnotherPoint = Point(2, 2)
    // val res1 = point != anotherPoint
    val res2 = point == point
    val res3 = point == yetAnotherPoint
    val res4 = yetAnotherPoint == yetAnotherPoint
    val twentyThreeBinary = 23.toBinaryString
    val twentyThreeHex = 23.toHexString
    val ingredient = ("Sugar", 25)
    println("ingredient: " + ingredient)
    println("ingredient._1: " + ingredient._1)
    val (name, quantity) = ingredient
    println("name: " + name + ", quantity: " + quantity)
    println("Should res1 be true or false? 1 for true 0 for false")
    val userInput = io.StdIn.readInt()
    var res1 = false
    if (userInput == 1) {
      res1 = true
    }
    else {
      res1 = false
    }
    println("Is res1 true? ")
    if (res1)
      Console.println(s"${RESET}${GREEN}${YELLOW_B}yes${RESET}")
    else
      Console.println(s"${RESET}${RED}${UNDERLINED}NO!${RESET}")

    println("point == point: " + res2)
    println("point == yetAnotherPoint: " + res3)
    println("yetAnotherPoint == yetAnotherPoint: " + res4)
    println("Binary 23: " + twentyThreeBinary)
    println("Hex 23: " + twentyThreeHex)

    val salaries = Seq(20000, 70000, 40000)
    //val doubleSalary = (x: Int) => x * 2
    val newSalaries = salaries.map(_ * 2)
    println("Original salaries: " + salaries)
    println("New salaries: " + newSalaries)

    val x: Int = Random.nextInt(10)

    x match {
      case 0 => "zero"
      case 1 => "one"
      case 2 => "two"
      case _ => "other"
    }

    def factorial(x: Int): Int = {
      def fact(x: Int, accumulator: Int): Int = {
        if (x <= 1) accumulator
        else fact(x - 1, x * accumulator)
      }
      fact(x, 1)
    }

    println("5!: " + factorial(5))
    println("11!: " + factorial(11))
    
//    val greeting: Option[String] = Some("Hello world")
//    println(greeting.get)
//
//    val greeting: Option[String] = None
//    println(greeting.get)
//    greeting.getOrElse("No greeting")

  }
}
