import java.util.*;
class Prac1{
static int XorAscii(String str, int len)
{

	int ans = 0;

	for (int i = 0; i < len; i++) {

		ans = (127 ^ ((str.charAt(i))));
	}
	return ans;
}

public static void main(String[] args)
{
	Scanner sc = new Scanner(System.in);

    System.out.println("Enter String : ");

    String str = sc.nextLine();
	int len = str.length();
	System.out.print(" XOR of given is : " +XorAscii(str, len) +"\n");

	
}
}

