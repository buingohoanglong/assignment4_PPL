.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()[[I
Label0:
	iconst_2
	anewarray [I
	dup
	iconst_0
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
	aastore
	dup
	iconst_1
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
	aastore
	areturn
Label1:
	return
.limit stack 11
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iconst_0
	istore_2
Label2:
	iload_2
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iconst_0
	istore_3
Label8:
	iload_3
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	invokestatic MCClass/foo()[[I
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label9:
Label10:
	iconst_1
	iload_3
	iadd
	istore_3
	goto Label8
Label11:
Label3:
Label4:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label2
Label5:
	invokestatic io/printLn()V
	invokestatic MCClass/foo()[[I
	iload_1
	iconst_1
	isub
	aaload
	iload_1
	iconst_1
	iadd
	bipush 7
	iastore
	iconst_0
	istore_2
Label14:
	iload_2
	iconst_2
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label17
	iconst_0
	istore_3
Label20:
	iload_3
	iconst_3
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label23
	invokestatic MCClass/foo()[[I
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label21:
Label22:
	iconst_1
	iload_3
	iadd
	istore_3
	goto Label20
Label23:
Label15:
Label16:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label14
Label17:
Label1:
	return
.limit stack 28
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
