.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [[I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	aastore
	putstatic MCClass/x [[I
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iconst_0
	istore_2
Label8:
	iload_2
	iconst_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	getstatic MCClass/x [[I
	iload_1
	aaload
	iload_2
	iload_1
	iload_2
	iadd
	iastore
Label9:
Label10:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label8
Label11:
Label3:
Label4:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label2
Label5:
	iconst_0
	istore_1
Label14:
	iload_1
	iconst_2
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label17
	iconst_0
	istore_2
Label20:
	iload_2
	iconst_2
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label23
	getstatic MCClass/x [[I
	iload_1
	aaload
	iload_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label21:
Label22:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label20
Label23:
Label15:
Label16:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label14
Label17:
Label1:
	return
	return
.limit stack 28
.limit locals 3
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
