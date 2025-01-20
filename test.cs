
using System;

namespace System
{
	/// <summary>Stellt einen Generator für Pseudozufallszahlen dar, d. h. ein Gerät, das eine Zahlenfolge erzeugt, die bestimmte statistische Anforderungen hinsichtlich ihrer Zufälligkeit erfüllt.</summary>
	// Token: 0x02000172 RID: 370
	public class Random
	{
		/// <summary>Initialisiert eine neue Instanz der <see cref="T:System.Random" />-Klasse unter Verwendung eines zeitabhängigen Standardstartwerts.</summary>
		// Token: 0x06000E95 RID: 3733 RVA: 0x0003BB5F File Offset: 0x00039D5F
		public Random() : this(Random.GenerateSeed())
		{
		}

		/// <summary>Initialisiert eine neue Instanz der <see cref="T:System.Random" />-Klasse unter Verwendung des angegebenen Startwerts.</summary>
		/// <param name="Seed">Eine Zahl, mit der ein Startwert für Folgen von Pseudozufallszahlen berechnet wird. Wenn eine negative Zahl angegeben wird, wird der absolute Wert der Zahl verwendet.</param>
		// Token: 0x06000E96 RID: 3734 RVA: 0x0003BB6C File Offset: 0x00039D6C
		public Random(int Seed)
		{
			int num = 0;
			int num2 = (Seed == int.MinValue) ? int.MaxValue : Math.Abs(Seed);
			int num3 = 161803398 - num2;
			this._seedArray[55] = num3;
			int num4 = 1;
			for (int i = 1; i < 55; i++)
			{
				if ((num += 21) >= 55)
				{
					num -= 55;
				}
				this._seedArray[num] = num4;
				num4 = num3 - num4;
				if (num4 < 0)
				{
					num4 += int.MaxValue;
				}
				num3 = this._seedArray[num];
			}
			for (int j = 1; j < 5; j++)
			{
				for (int k = 1; k < 56; k++)
				{
					int num5 = k + 30;
					if (num5 >= 55)
					{
						num5 -= 55;
					}
					this._seedArray[k] -= this._seedArray[1 + num5];
					if (this._seedArray[k] < 0)
					{
						this._seedArray[k] += int.MaxValue;
					}
				}
			}
			this._inext = 0;
			this._inextp = 21;
			Seed = 1;
		}

		/// <summary>Gibt eine zufällige Gleitkommazahl zwischen 0,0 und 1,0 zurück.</summary>
		/// <returns>Eine Gleitkommazahl mit doppelter Genauigkeit, die größer oder gleich 0,0 und kleiner als 1,0 ist.</returns>
		// Token: 0x06000E97 RID: 3735 RVA: 0x0003BC7F File Offset: 0x00039E7F
		protected virtual double Sample()
		{
			return (double)this.InternalSample() * 4.656612875245797E-10;
		}

		// Token: 0x06000E98 RID: 3736 RVA: 0x0003BC94 File Offset: 0x00039E94
		private int InternalSample()
		{
			int num = this._inext;
			int num2 = this._inextp;
			if (++num >= 56)
			{
				num = 1;
			}
			if (++num2 >= 56)
			{
				num2 = 1;
			}
			int num3 = this._seedArray[num] - this._seedArray[num2];
			if (num3 == 2147483647)
			{
				num3--;
			}
			if (num3 < 0)
			{
				num3 += int.MaxValue;
			}
			this._seedArray[num] = num3;
			this._inext = num;
			this._inextp = num2;
			return num3;
		}

		// Token: 0x06000E99 RID: 3737 RVA: 0x0003BD08 File Offset: 0x00039F08
		private static int GenerateSeed()
		{
			Random random = Random.t_threadRandom;
			if (random == null)
			{
				Random obj = Random.s_globalRandom;
				int seed;
				lock (obj)
				{
					seed = Random.s_globalRandom.Next();
				}
				random = new Random(seed);
				Random.t_threadRandom = random;
			}
			return random.Next();
		}

		// Token: 0x06000E9A RID: 3738 RVA: 0x0003BD68 File Offset: 0x00039F68
		private unsafe static int GenerateGlobalSeed()
		{
			int result;
			Interop.GetRandomBytes((byte*)(&result), 4);
			return result;
		}

		/// <summary>Gibt eine nicht negative Zufallsganzzahl zurück.</summary>
		/// <returns>Eine ganze 32-Bit-Zahl mit Vorzeichen, die größer oder gleich 0 (null) und kleiner als <see cref="F:System.Int32.MaxValue" /> ist.</returns>
		// Token: 0x06000E9B RID: 3739 RVA: 0x0003BD7F File Offset: 0x00039F7F
		public virtual int Next()
		{
			return this.InternalSample();
		}

		// Token: 0x06000E9C RID: 3740 RVA: 0x0003BD88 File Offset: 0x00039F88
		private double GetSampleForLargeRange()
		{
			int num = this.InternalSample();
			if (this.InternalSample() % 2 == 0)
			{
				num = -num;
			}
			return ((double)num + 2147483646.0) / 4294967293.0;
		}

		/// <summary>Gibt eine Zufallsganzzahl zurück, die in einem angegebenen Bereich liegt.</summary>
		/// <param name="minValue">Die inklusive untere Grenze der zurückgegebenen Zufallszahl.</param>
		/// <param name="maxValue">Die exklusive obere Grenze der zurückgegebenen Zufallszahl. <paramref name="maxValue" /> muss größer oder gleich <paramref name="minValue" /> sein.</param>
		/// <returns>Eine 32-Bit-Ganzzahl mit Vorzeichen, die größer oder gleich <paramref name="minValue" /> und kleiner als <paramref name="maxValue" /> ist, d. h., der Bereich der Rückgabewerte umfasst <paramref name="minValue" />, aber nicht <paramref name="maxValue" />. Wenn <paramref name="minValue" /> gleich <paramref name="maxValue" /> ist, wird <paramref name="minValue" /> zurückgegeben.</returns>
		/// <exception cref="T:System.ArgumentOutOfRangeException">
		///   <paramref name="minValue" /> ist größer als <paramref name="maxValue" />.</exception>
		// Token: 0x06000E9D RID: 3741 RVA: 0x0003BDC8 File Offset: 0x00039FC8
		public virtual int Next(int minValue, int maxValue)
		{
			if (minValue > maxValue)
			{
				throw new ArgumentOutOfRangeException("minValue", SR.Format("'{0}' cannot be greater than {1}.", "minValue", "maxValue"));
			}
			long num = (long)maxValue - (long)minValue;
			if (num <= 2147483647L)
			{
				return (int)(this.Sample() * (double)num) + minValue;
			}
			return (int)((long)(this.GetSampleForLargeRange() * (double)num) + (long)minValue);
		}

		/// <summary>Gibt eine nicht negative Zufallsganzzahl zurück, die kleiner als das angegebene Maximum ist.</summary>
		/// <param name="maxValue">Die exklusive obere Grenze der Zufallszahl, die generiert werden soll. <paramref name="maxValue" /> muss größer oder gleich 0 sein.</param>
		/// <returns>Eine ganze 32-Bit-Zahl mit Vorzeichen, die größer oder gleich 0 (null) und kleiner als <paramref name="maxValue" /> ist, d.h., der Bereich der Rückgabewerte umfasst in der Regel 0 (null), aber nicht <paramref name="maxValue" />. Wenn jedoch <paramref name="maxValue" /> 0 (null) entspricht, wird <paramref name="maxValue" /> zurückgegeben.</returns>
		/// <exception cref="T:System.ArgumentOutOfRangeException">
		///   <paramref name="maxValue" /> ist kleiner als 0.</exception>
		// Token: 0x06000E9E RID: 3742 RVA: 0x0003BE22 File Offset: 0x0003A022
		public virtual int Next(int maxValue)
		{
			if (maxValue < 0)
			{
				throw new ArgumentOutOfRangeException("maxValue", SR.Format("'{0}' must be greater than zero.", "maxValue"));
			}
			return (int)(this.Sample() * (double)maxValue);
		}

		/// <summary>Gibt eine zufällige Gleitkommazahl zurück, die größer oder gleich 0,0 und kleiner als 1,0 ist.</summary>
		/// <returns>Eine Gleitkommazahl mit doppelter Genauigkeit, die größer oder gleich 0,0 und kleiner als 1,0 ist.</returns>
		// Token: 0x06000E9F RID: 3743 RVA: 0x0003BE4C File Offset: 0x0003A04C
		public virtual double NextDouble()
		{
			return this.Sample();
		}

		/// <summary>Füllt die Elemente eines angegebenen Bytearrays mit Zufallszahlen.</summary>
		/// <param name="buffer">Ein Bytearray, das für Zufallszahlen vorgesehen ist.</param>
		/// <exception cref="T:System.ArgumentNullException">
		///   <paramref name="buffer" /> ist <see langword="null" />.</exception>
		// Token: 0x06000EA0 RID: 3744 RVA: 0x0003BE54 File Offset: 0x0003A054
		public virtual void NextBytes(byte[] buffer)
		{
			if (buffer == null)
			{
				throw new ArgumentNullException("buffer");
			}
			for (int i = 0; i < buffer.Length; i++)
			{
				buffer[i] = (byte)this.InternalSample();
			}
		}

		// Token: 0x06000EA1 RID: 3745 RVA: 0x0003BE88 File Offset: 0x0003A088
		public unsafe virtual void NextBytes(Span<byte> buffer)
		{
			for (int i = 0; i < buffer.Length; i++)
			{
				*buffer[i] = (byte)this.Next();
			}
		}

		// Token: 0x040012C4 RID: 4804
		private const int MBIG = 2147483647;

		// Token: 0x040012C5 RID: 4805
		private const int MSEED = 161803398;

		// Token: 0x040012C6 RID: 4806
		private const int MZ = 0;

		// Token: 0x040012C7 RID: 4807
		private int _inext;

		// Token: 0x040012C8 RID: 4808
		private int _inextp;

		// Token: 0x040012C9 RID: 4809
		private int[] _seedArray = new int[56];

		// Token: 0x040012CA RID: 4810
		[ThreadStatic]
		private static Random t_threadRandom;

		// Token: 0x040012CB RID: 4811
		private static readonly Random s_globalRandom = new Random(Random.GenerateGlobalSeed());
	}
}
