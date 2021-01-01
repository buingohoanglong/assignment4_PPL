.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 8
	istore_1
Label0:
	iload_1
	iconst_4
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label2
.var 2 is y I from Label0 to Label1
	iconst_0
	istore_2
	iload_2
	istore_1
	goto Label5
Label2:
	iload_1
	iconst_4
	irem
	iconst_1
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
.var 3 is y I from Label0 to Label1
	iconst_1
	istore_3
	iload_3
	istore_1
	goto Label5
Label3:
	iload_1
	iconst_4
	irem
	iconst_2
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label4
.var 4 is y I from Label0 to Label1
	iconst_2
	istore 4
	iload 4
	istore_1
	goto Label5
Label4:
.var 5 is y I from Label0 to Label1
	iconst_3
	istore 5
	iload 5
	istore_1
Label5:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 16
.limit locals 6
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
