.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	astore_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	astore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	aload_1
	astore_2
	aload_1
	iconst_1
	bipush 10
	iastore
	iconst_0
	istore_3
Label4:
	iload_3
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label2:
	aload_1
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label3:
	iconst_1
	iload_3
	iadd
	istore_3
	goto Label4
Label5:
	invokestatic io/printLn()V
	iconst_0
	istore_3
Label10:
	iload_3
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
Label8:
	aload_1
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label9:
	iconst_1
	iload_3
	iadd
	istore_3
	goto Label10
Label11:
Label1:
	return
.limit stack 21
.limit locals 4
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
