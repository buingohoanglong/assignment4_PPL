.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [I

.method public static sum([I)I
.var 0 is x [I from Label0 to Label1
.var 1 is s I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iconst_0
	istore_2
Label2:
	iload_2
	iconst_5
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iload_1
	aload_0
	iload_2
	iaload
	iadd
	istore_1
Label3:
Label4:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label2
Label5:
	iload_1
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_5
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
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	putstatic MCClass/x [I
.var 1 is y I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	getstatic MCClass/x [I
	invokestatic MCClass/sum([I)I
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
	return
.limit stack 9
.limit locals 2
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
