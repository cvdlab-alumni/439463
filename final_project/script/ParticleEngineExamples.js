Examples =
{

	
	// (1) build GUI for easy effects access.
	// (2) write ParticleEngineExamples.js
	
	// Not just any fountain -- a RAINBOW STAR FOUNTAIN of AWESOMENESS

	fireball :
	{
		positionStyle  : Type.SPHERE,
		positionBase   : new THREE.Vector3( 71.3,58,7),
		positionRadius : 2,
				
		velocityStyle : Type.SPHERE,
		speedBase     : 1,
		speedSpread   : 0.5,
		
		particleTexture : THREE.ImageUtils.loadTexture( 'assets/textures/general/smoke512.png' ),

		sizeTween    : new Tween( [0, 0.1], [1, 3] ),
		opacityTween : new Tween( [0.7, 1], [1, 0] ),
		colorBase    : new THREE.Vector3(0.02, 1, 0.4),
		blendStyle   : THREE.AdditiveBlending,  
		
		particlesPerSecond : 60,
		particleDeathAge   : 2,		
		emitterDeathAge    : 60
	},

	fornello :
	{
/*
		var z = Math.random();
		var t = 6.2832 * Math.random();
		var r = 0.1;
		var vec3 = new THREE.Vector3(4*r * Math.cos(t), 4*r * Math.sin(t), r );


*/
		positionStyle  : Type.SPHERE,
		//positionBase   : new THREE.Vector3( 71, -6, 56 ),
		positionBase   : new THREE.Vector3( 12.85,26.5,7.5 ),
		//positionBase : new THREE.Vector3(0,2,0),
		positionRadius : 2,
				
		velocityStyle : Type.SPHERE,
		velocityBase   : new THREE.Vector3(0,0,10),
		velocitySpread : new THREE.Vector3(1,0,1),
		
		particleTexture : THREE.ImageUtils.loadTexture( 'assets/textures/general/smoke512.png' ),

		sizeTween    : new Tween( [0, 0.3, 1.2], [1, 1, 2]),
		opacityTween : new Tween( [0.7, 1], [1, 0.9] ),
		colorBase    : new THREE.Vector3(0.02, 1, 0.4),
		blendStyle   : THREE.AdditiveBlending,  
		
		particlesPerSecond : 60,
		particleDeathAge   : 1.5,		
		emitterDeathAge    :5

	}
/*
	fireball :
	{
		positionStyle  : Type.SPHERE,
		//positionBase   : new THREE.Vector3( 71, -6, 56 ),
		positionBase   : new THREE.Vector3( 71.5,58,40 ),
		//positionBase : new THREE.Vector3(0,2,0),
		positionRadius : 2,
				
		velocityStyle : Type.SPHERE,
		velocityBase   : 40,
		velocitySpread : 8,
		
		particleTexture : THREE.ImageUtils.loadTexture( 'assets/textures/general/smoke512.png' ),

		sizeTween    : new Tween( [0, 0.1], [1, 150] ),
		opacityTween : new Tween( [0.7, 1], [1, 0.9] ),
		colorBase    : new THREE.Vector3(0.02, 1, 0.4),
		blendStyle   : THREE.AdditiveBlending,  
		
		particlesPerSecond : 100,
		particleDeathAge   : 1.5,		
		emitterDeathAge    : 60

	}
*/

	/*
	fornello :
	{

		var z = Math.random();
		var t = 6.2832 * Math.random();
		var r = 0.1;
		var vec3 = new THREE.Vector3(4*r * Math.cos(t), 4*r * Math.sin(t), r );



		positionStyle  : Type.SPHERE,
		//positionBase   : new THREE.Vector3( 71, -6, 56 ),
		positionBase   : new THREE.Vector3( 73,55,2 ),
		//positionBase : new THREE.Vector3(0,2,0),
		positionRadius : 2,
				
		velocityStyle : Type.SPHERE,
		velocityBase   : new THREE.Vector3(0,0,10),
		velocitySpread : new THREE.Vector3(1,0,1),
		
		particleTexture : THREE.ImageUtils.loadTexture( 'assets/textures/general/smoke512.png' ),

		sizeTween    : new Tween( [0, 0.3, 1.2], [1, 1, 2]),
		opacityTween : new Tween( [0.7, 1], [1, 0.9] ),
		colorBase    : new THREE.Vector3(0.02, 1, 0.4),
		blendStyle   : THREE.AdditiveBlending,  
		
		particlesPerSecond : 60,
		particleDeathAge   : 1.5,		
		emitterDeathAge    : 60

	}*/	
}